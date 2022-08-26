"""Extract Nat Policies"""

from typing import List
from pandevice import panorama

from paloaltoapi import config
from paloaltoapi.utils import get_version
from paloaltoapi.statics import RULEBASE
from paloaltoapi.exceptions import ParamsError
from . import assign_locations_for_rules, get_config_entries
from .policy import NatRule

class NatPolicies:
    """
    NAT Policy Module
    """
    def __init__(self, device: str, key: str, version: str = None,
                 certstore=None):
        """
        Set up palo alto NAT Policy OBject from Panorama\n
        Keyword Arguments:
        ------------
            \tdevice {str} -- FQDN of Panorama Object\n
            \tkey {str} -- Palo Alto API Key\n
            \tversion {str} -- Palo Alto major release version ex: 9.x 10.x (default: {None})\n
            \tcertstore {str|bool} -- Verification on/off or supply
             custom cert store fore SSL (default: {None})
        """
        if not version:
            version = get_version(
                device=device,api_key=key)
        self.version = version
        self.device = device
        self.nat_policies = { }
        self.api_key = key
        self.certstore = certstore if certstore else config.CERT
        self.pano = panorama.Panorama(self.device, api_key=self.api_key)

    def get_nat_rules(self, device_group: list, rulebase: str,
                      name: str = None, uuid: str = None):
        """
        Get NAT Rules based off name or uuid
        """
        if name and uuid:
            raise ParamsError(f'Only enter one param name={name} uuid={uuid}')
        if name or uuid:
            raise ParamsError(f'Requires one param name={name} uuid={uuid}')
        if rulebase not in RULEBASE:
            raise ParamsError(f'Bad rulebase={rulebase}')
        for devgrp in device_group:
            self.pano.add(panorama.DeviceGroup(devgrp))

    def search_nat_rules(self, members: List[str]) -> dict:
        """
        :param members: [description]
        :type members: [str]
        :return: [description]
        :rtype: dict
        """
        result = []
        rule_queries = []

        for member in members:
            # Used to search the member type in the NAT field
            rule_queries.append(f'(destination//member[.="{member}"])or(source//member[.="{member}"])')
            # Used to search translation addresses
            rule_queries.append(
                f'(destination-translation//translated-address[.="{member}"])or(source-translation//translated-address[.="{member}"])')

        rule_query = "or".join(rule_queries)
        # changed: print(rule_queries)
        searches = config.GLOBAL_SEARCHES["nat"]
        # changed: print(searches)
        for search in searches:
            rules = get_config_entries(
                device=self.device,
                xpath=search["xpath"].format(rule_query),
                api_key=self.api_key
            )
            # changed: print(rules)
            for entry in rules:
                tmp = {}
                tmp["location"] = search["location"]
                tmp["location-type"] = search["location-type"]
                clean_entry = NatRule({**entry, **tmp})
                result.append(clean_entry.clean_entry)
        assign_locations_for_rules(result, api_key=self.api_key,device=self.device)
        return {"amount": len(result), "result": result}

def __check_uri_length(url: str):
    """
    :param url: Checks URL/URI length prior to trying to serve request
    :type url: str
    :return: True if passes
    :rtype: bool
    """
    # Changed: return True if len(url) < 2048 else False
    return bool(len(url) < 2048)
