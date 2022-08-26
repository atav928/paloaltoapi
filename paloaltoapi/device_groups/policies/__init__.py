"""Polices Init file"""
from collections import OrderedDict
from typing import Any, Dict
import re
import requests
import xmltodict

from panos.panorama import Panorama as PanosPanorama

from paloaltoapi import config
from paloaltoapi.commit import set_audit_comment
from paloaltoapi.exceptions import PaloAltoMissingParam
from paloaltoapi.statics import RULEBASE
from paloaltoapi.utils import xml_call

class VersionParam:
    def __init__(self, name, default=None, version=None):
        self.name = name.replace("-","_")
        self.default = default
        self.value = None

class NatRuleTest:
    """NAT Rule

    Both the naming convention and the order of the parameters tries to closly
    match what is presented in the GUI.

    There are groupings of parameters that give hints to the sections that
    they contribute towards:

        * source_translation_<etc>
        * source_translation_fallback_<etc>
        * source_translation_static_<etc>
        * destination_translation_<etc>

    Args:
        name (str): Name of the rule
        description (str): The description
        nat_type (str): Type of NAT
        fromzone (list): From zones
        tozone (list): To zones
        to_interface (str): Egress interface from route lookup
        service (str): The service
        source (list): Source addresses
        destination (list): Destination addresses
        source_translation_type (str): Type of source address translation
        source_translation_address_type (str): Address type for Dynamic IP
            And Port or Dynamic IP source translation types
        source_translation_interface (str): Interface of the source address
            translation for Dynamic IP and Port source translation types
        source_translation_ip_address (str): IP address of the source address
            translation for Dynamic IP and Port source translation types
        source_translation_translated_addresses (list): Translated addresses
            of the source address translation for Dynamic IP And Port or
            Dynamic IP source translation types
        source_translation_fallback_type (str): Type of fallback for Dynamic IP
            source translation types
        source_translation_fallback_translated_addresses (list): Addresses for
            translated address types of fallback source translation
        source_translation_fallback_interface (str): The interface for the
            fallback source translation
        source_translation_fallback_ip_type (str): The type of the IP address
            for the fallback source translation IP address
        source_translation_fallback_ip_address (str): The IP address of the
            fallback source translation
        source_translation_static_translated_address (str): The IP address
            for the static source translation
        source_translation_static_bi_directional (bool): Allow reverse
            translation from translated address to original address
        destination_translated_address (str): Translated destination IP
            address
        destination_translated_port (int): Translated destination port number
        ha_binding (str): Device binding configuration in HA Active-Active mode
        disabled (bool): Disable this rule
        negate_target (bool): Target all but the listed target firewalls
            (applies to panorama/device groups only)
        target (list): Apply this policy to the listed firewalls only
            (applies to panorama/device groups only)
        tag (list): Administrative tags
        destination_dynamic_translated_address (str): (PAN-OS 8.1+) Dynamic
            destination translated address.
        destination_dynamic_translated_port (int): (PAN-OS 8.1+) Dynamic
            destination translated port.
        destination_dynamic_translated_distribution (str): (PAN-OS 8.1+) Dynamic
            destination translated distribution.
        uuid (str): (PAN-OS 9.0+) The UUID for this rule.
        group_tag (str): (PAN-OS 9.0+) The group tag.
    """
    def __init__(self, rule: dict, version: str):
        self.__rule = rule
        self.name = rule.get('@name', None)
        self.uuid = rule.get('@uuid', None)
        self.location = rule.get('location', '')
        self.device_group = rule.get('location_type', '')
        self.from_zone = rule['from'].get('member', ['any'])
        self.to_zone = rule['to'].get('member', ['any'])
        self.source = rule['source'].get('member', ['any'])
        self.destination = rule['destination'].get('member', ['any'])
        self.get_dest_translation(rule)

    def get_dest_translation(self, rule: dict):
        if rule.get('destination-translation'):
            rule['destination-translation']

    def change_name(self, name):
        return name.replace('-', '_')

    def __repr__(self) -> str:
        attrs = str([x for x in self.__dict__])
        return "<paloaltoapi.policies.NatRule: > {} ".format(attrs)


def change_keys(obj, convert):
    """
    Recursively goes through the dictionary obj and replaces keys with the convert function.
    """
    if isinstance(obj, (str, int, float)):
        return obj
    if isinstance(obj, dict):
        new = obj.__class__()
        for key, value in obj.items():
            new[convert(key)] = change_keys(value, convert)
    elif isinstance(obj, (list, set, tuple)):
        new = obj.__class__(change_keys(v, convert) for v in obj)
    else:
        return obj
    return new

def delete_obj_from_rule(rule: dict, **kwargs):
    """
    :params rule:
    :params device:
    :params api_key:
    :params verify:
    """
    action = 'delete'
    try:
        device=kwargs['device']
        api_key=kwargs['api_key']
        change_num = kwargs.get('chg_number', 'CHG1234567')
        verify=kwargs.get('verify', None)
        rulename = rule['@name']
        rulebase = rule['rulebase']
        device_grp = rule['location']
        member_loc = rule['member_location']
        member = rule['search_value']
    except KeyError as err:
        raise PaloAltoMissingParam(err)
    if device_grp == 'shared':
        xpath = config.SECURITY_RULES[action]['shared'].format(rulebase,rulename,
                                                        member_loc,member)
    else:
        xpath = config.SECURITY_RULES[action]['device-group'].format(device_grp,
                                rulebase,rulename,member_loc,member)
    resp = xml_call(device,xpath,api_key,action=action,certstore=verify)
    audit_resp = set_audit_comment(device=device,api_key=api_key,rule=rulename,
                                    location=device_grp,rulebase=rulebase,
                                    change_num=change_num)
    # Add Audit Response to the result
    if audit_resp.get('status') == 'success' or audit_resp.get('@status') == 'success':
        audit_msg = audit_resp.get('result', 'Unknown')
    else:
        audit_msg = 'ERROR'
    result = {'response': return_rule_response(resp,action=action,location=device_grp,
                        member_location=member_loc,rule=rulename,
                        member=member,audit_msg=audit_msg)}
    return result

def add_obj_to_rule(rule: dict, **kwargs):
    """
    :params rule:
    :params device:
    :params api_key:
    :params verify:
    """
    action = 'set'
    try:
        device=kwargs['device']
        api_key=kwargs['api_key']
        change_num = kwargs.get('change_num', 'CHG1234567')
        verify=kwargs.get('verify', None)
        rulename = rule['@name']
        rulebase = rule['rulebase']
        device_grp = rule['location']
        member_loc = rule['member_location']
        member = rule['search_value']
    except KeyError as err:
        raise PaloAltoMissingParam(err)
    params = {'element': config.ADDRESS_GROUP['element'].format(member)}
    if rule['location'] == 'shared':
        xpath = config.SECURITY_RULES[action]['shared'].format(rulebase,rulename,
                                                        member_loc)
    else:
        xpath = config.SECURITY_RULES[action]['device-group'].format(device_grp,
                                rulebase,rulename,member_loc)
    resp = xml_call(device,xpath,api_key,action=action,certstore=verify,params=params,
                    param_type='config')
    audit_resp = set_audit_comment(device=device,api_key=api_key,rule=rulename,
                                    location=device_grp,rulebase=rulebase,
                                    change_num=change_num)
    # Add Audit Response to the result
    if audit_resp.get('status') == 'success' or audit_resp.get('@status') == 'success':
        audit_msg = audit_resp.get('result', 'Unknown')
    else:
        audit_msg = 'ERROR'
    result = {'response': return_rule_response(resp,action=action,location=device_grp,
                        member_location=member_loc,rule=rulename,
                        member=member,audit_msg=audit_msg)}
    return result

def assign_locations_for_rules(result: list, api_key: str,device:str) -> Dict[str, Any]:
    """
    Returns a location and rulebase of a uuid object can work on Security or NAT Rules.
    :param result: [description]
    :type result: str
    """
    for rule in result:
        rule['rulebase'] = ""
        # Cycle through and check rule against each rulebase to
        # find the rulebase and device group
        for rbase in RULEBASE:
            if rule['location-type'] == 'shared':
                rule['location'] = "shared"
                xpath = config.GLOBAL_SEARCHES['rule_location_shared']['xpath'].format(
                    rbase, rule['@uuid'])
            else:
                rule['location'] = ""
                xpath = config.GLOBAL_SEARCHES['rule_location']['xpath'].format(
                    rbase, rule['@uuid'])
            entries = get_config_entries(device=device,xpath=xpath, api_key=api_key)
            # sets the entry values
            if len(entries) == 1:
                rule['location'] = entries[0]["@name"]
                rule['rulebase'] = rbase
                break

def get_config_entries(device:str, xpath: str, api_key: str) -> dict:
    """
    :param xpath: Supply formated xpath for request
    :type xpath: str
    :return: response
    :rtype: dict
    """
    entries = []
    result = get_config(device=device, xpath=xpath, api_key=api_key)
    if result["result"] is None:
        entries = []
    elif int(result["result"]["@count"]) == 1:
        entries.append(result["result"]["entry"])
    else:
        entries = result["result"]["entry"]
    return entries

def get_config(device: str, xpath: str, api_key: str,
               certstore = config.CERT) -> dict:
    """
    :param xpath: XPATH param for XML call
    :type xpath: str
    :return: Palo Alto Response from equests library
    :rtype: dict
    """
    params = {
        "type": "config",
        "action": "get",
        "xpath": xpath
    }
    headers = {
        'X-PAN-KEY': api_key
    }
    url = f"https://{device}/api/"
    method="POST"
    try:
        res = requests.request(
            url=url,
            method=method,
            headers=headers,
            params=params,
            verify=certstore
        )
        #print(res.json())
        res.raise_for_status()
        # removed: print(xmltodict.parse(res.text)["response"])
    except Exception as err:
        raise Exception(str(err).replace(api_key, "***"))
    return xmltodict.parse(res.text)["response"]

def return_rule_response(message: OrderedDict, action: str, member: str, member_location: str,
                        location: str,rule: str, audit_msg: str) -> Dict[str,str]:
    """reformats the response"""
    result_list =['status','message','member','member_location','rule','location']
    result = {r: None for r in result_list}
    result['status'] = message['@status']
    result['action'] = 'add' if action == 'set' else action
    result['member'] = member
    result['member_location'] = member_location
    result['rule'] = rule
    result['location'] = location
    result['message'] = message['msg']
    result['audit'] = audit_msg
    return result

def check_chg_number(change: str) -> bool:
    """Checks that the change supplied is correctly formated.

    Args:
        change (str): SNOW Change or Incedent Number

    Returns:
        bool: True if it is valid
    """
    regex = r'^(CHG|INC)[0-9]{7}$'
    return bool(re.match(regex,change))
