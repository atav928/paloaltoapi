"""Get Dyanmic tags register and unregister them"""
from typing import List

from paloaltoapi import config
from paloaltoapi.formatter import extract_registered_ip
from paloaltoapi.urls import Url

class AutoTags:
    """
    Class used to handle automatic tagging for DAG
    """
    def __init__(self, device:str, api_key: str, is_panorama: bool = False,
                certstore=None):
        """
        We use panorama bool value to determine if
        device group is a required field or not
        """
        # TODO: Update how to differencitate between Palo Alto and Firewall
        self.is_panorama = is_panorama
        self.device = device
        self.api_key = api_key
        self.certstore = certstore if certstore is not None else config.CERT
        self.all_dynamic_tags = {}
        self.registered_ip_list = []
        self.registered_ip = None
        self.testing_return = None
        self.registered_ip_response = None
        self.removed_registered_ip_list = None
        self.removed_registered_ip = None
        self.unregistered_ip_response = None

    def get_dynamic_tags(self, name: str = 'all'):
        """
        if all we are going to search everything and parse into their device group
        if not then we are going to just get that name and extract it into the json
        """
        self.testing_return = Url.xml_get_dynamic_address_group(device=self.device,
                                        api_key=self.api_key,
                                        name=name, cert=self.certstore)

    def get_registered_ip(self, tag: str) -> list:
        """Get registered IP from a specific tag name

        Args:
            tag (str): name of tag.

        Returns:
            _type_: list of IP's associated with that DAG/Tag
        """
        self.registered_ip = Url.xml_get_registered_ip(device=self.device,
                                                api_key=self.api_key,
                                                tag=tag, cert=self.certstore)
        self.registered_ip_list = extract_registered_ip(self.registered_ip)
        return self.registered_ip_list

    def delete_registered_ip(self, tag: str, ip_list: List[str]):
        """Delete unregister an IP from a tag/dag name

        Args:
            tag (str): name of DAG/Tag to delete from
            ip_list (List[str]): list of IP's that need to be removed
        """
        if not isinstance(ip_list, list):
            ip_list=[ip_list]
        req = Url.xml_delete_registered_ip(device=self.device, api_key=self.api_key,
                            tag=tag, ip_list=ip_list, cert=self.certstore)
        #print(req)
        self.registered_ip_response = req
        # Compare new vs old
        new_list = extract_registered_ip(Url.xml_get_registered_ip(device=self.device,
                                                api_key=self.api_key,
                                                tag=tag, cert=self.certstore))
        self.removed_registered_ip = set(self.registered_ip_list).difference(new_list)
        self.removed_registered_ip_list = new_list

    def add_registered_ip(self, tag: str, ip_list: List[str],
                    persistent: int = 0, timeout:int = 0):
        """
        Add a registered IP to a dynamic tag.
        Params
        ------
        param tag: Palo Alto Dynamic Tag name. Case sensitive.
        type tag: str
        param ip_list: Array of IP Addresses needed to add to the tag.
        type ip_list: Array of Strings
        param persistent: The default is 1, which means that the tagging will
            survive reboots of the Firewall. Options 0 or 1.
        type persistent: int
        param timeout: optional timeout parameter, to specify the expiration
            in seconds of the tag. The default is 0, which means 'never expire'.
            The maximum value is 2592000 (30 days).
        type timeout: int
        """
        if not isinstance(ip_list, list):
            ip_list=[ip_list]
        req = Url.xml_add_registered_ip(device=self.device, api_key=self.api_key,
                            tag=tag, ip_list=ip_list, persistent=persistent,
                            timeout=timeout, cert=self.certstore)
        print(req.content)
        self.unregistered_ip_response = req
        # Compare new vs old
        new_list = extract_registered_ip(Url.xml_get_registered_ip(
                                        device=self.device, api_key=self.api_key,
                                        tag=tag, cert=self.certstore))
        self.removed_registered_ip = set(self.registered_ip_list).difference(new_list)
        print("The following was removed:", self.removed_registered_ip)
        print('Updating current registered list')
        self.removed_registered_ip_list = new_list
