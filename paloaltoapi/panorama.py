"""Panorama Module"""
import sys
from typing import Any, Dict
from bs4 import BeautifulSoup as BS
from paloaltoapi.commit import commit_panorama_device_group
from paloaltoapi.xmlparser import xml2dict
from paloaltoapi.firewall import Firewall
from paloaltoapi.urls import Url, ApiCalls
from paloaltoapi.exceptions import PaloAltoAPIError
from paloaltoapi.device_groups.device_group import DeviceGroup
from paloaltoapi.device_groups.objects.urlcategory.url_categories import UrlCategories
from paloaltoapi.highavail import HighAvail

class Panorama(Firewall):
    """
    Panorama
    """
    def __init__(self, device, username=None, passwd=None, certstore=False, key=None):
        """
        params device:
        """
        super().__init__(device=device, username=username,
                passwd=passwd, certstore=certstore, key=key)
        self.configs = {}
        self.high_avail_status()

    def __repr__(self):
        attrs = str([x for x in self.__dict__])
        return "<paloaltoapi.panorama.Panorama: {}> {} ".format(str(self), attrs)

    def _get_device_groups_from_pa(self) -> dict:
        values = Url.xml_device_entries(self.device, self.api_key)
        req = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                            params=values.get('params', None),
                            headers=values.get('headers', None),
                            data=values.get('data', None))
        soup = BS(req.text, features='html.parser')
        return xml2dict(str(soup))

    def get_device_group_list(self):
        try:
            xmldict = self._get_device_groups_from_pa()
            device_groups =  [ dg.get('name') for dg
                in xmldict['result']['device-group']['entry'] ]
            device_groups.append('shared')
        except (AttributeError, KeyError) as err:
            raise PaloAltoAPIError from err
        return device_groups

    def device_groups(self, device_list: list = None):
        """
        Device Group
        """
        if not device_list:
            device_groups = self.get_device_group_list()
        else:
            xmldict = self._get_device_groups_from_pa()
            device_groups = []
            for i in device_list:
                if not i in [ dg.get('name') for dg in
                    xmldict['result']['device-group']['entry'] ]:
                    raise PaloAltoAPIError(f"{device_groups} not a valid device group")
                else:
                    device_groups.append(i)
        try:
            # device_groups = device_list if device_list != None else
            #  [ dg.get('name') for dg in self.device_groups_map.key() ]
            self.DeviceGroups = DeviceGroup(
                device_list=device_groups, device=self.device, key=self.api_key)
            device_dict = {dg: {"policy":
                        {'security': {"pre-rules":
                            {"entry": []}, "post-rules": {"entry": []} }}}
                                for dg in device_groups}
            self.configs = { **self.configs, **device_dict }
        except (AttributeError, KeyError) as err:
            raise PaloAltoAPIError from err

    def __create_url_category_obj(self):
        try:
            getattr(self, "UrlCategories")
        except AttributeError:
            self.UrlCategories = UrlCategories(
                self.device, self.api_key, self.version, self.certstore)

    def url_categories(self):
        """
        Creates a UrlCategory Obj if one is not created to activate subcommands
        """
        self.__create_url_category_obj()

    def get_url_categories(self, device_group: str = None, name:str = None) -> dict:
        """
        Runs function to retrieve either a full Device Group list of URLS or
         returns just a single name'ed url category if specified. If pulling
         a full list back you'll also update the current config dictionary as
         well as update the subclass UrlCategories.url_cagetories dictionary.
        """
        self.__create_url_category_obj()

        # Call corresponding url function
        if not device_group:
            pass
        elif not name:
            self._get_url_all(device_group=device_group)
        else:
            self._get_url_by_name(device_group=device_group,
                        name=name)

    def _get_url_all(self, device_group: str) -> dict:
        """
        Get All URL
        """
        tmp = self.UrlCategories._get_url_cust_categories(
            device_group=device_group)
        if device_group not in self.configs.keys():
            self.configs.update({device_group: {"objects": {"url-categories": {"entry": tmp }}}})
        else:
            # find a way to search through the existing entries and
            #  current returned entry to see if one exists
            #  add it only if it is new for now just overright the returns
            #for entry in self.configs[device_group]['objects']['url-categories']['entry']
            self.configs[device_group].update({'objects': {'url-categories': {'entry': tmp }}})
            # self.configs[device_group]['objects']['url-categories']['entry'] = tmp
        return tmp

    def __update_url_cat_config(self, url_cat: dict):
        """
        Update URL
        """
        for device_group in url_cat.keys():
            if device_group not in self.configs.keys():
                self.configs.update({device_group: {"objects":
                        {"url-categories": {"entry": 
                                self.UrlCategories.url_categories[device_group]}}}})
            else:
                self.configs[device_group].update({'objects':
                        {'url-categories': {'entry': 
                                self.UrlCategories.url_categories[device_group]}}})

    def _get_url_by_name(self, device_group: str, name: str) -> dict:
        """
        Get URL
        """
        return self.UrlCategories._get_url_cust_categories_by_name(
            device_group=device_group, name=name)

    def high_avail_status(self):
        """
        Set HA Status
        """
        values = Url.xml_ha_get_status(self.device, self.api_key)
        req = ApiCalls.request_get(url=values['url'],
                                params=values.get('params', None),
                                headers=values.get('headers', None),
                                verify=self.certstore)
        soup = BS(req.text, features='html.parser')
        try:
            #print(soup)
            xmldict = xml2dict(str(soup))
            #print(xmldict)
            #if self.model not in PANORAMA:
            #    raise PaloAltoAPIError(f'{self.device} is not a Panorama device use Firewall')
            self.high_avail = HighAvail(xmldict, self.device,
                                        self.api_key, is_panorama=True)
        except AttributeError as err:
            raise PaloAltoAPIError from err
        except TypeError as err:
            sys.exit(err)

    def update_config(self, url_categories: bool = False) -> None:
        """
        Update Config
        """
        if url_categories:
            self.__create_url_category_obj()
            for device_group in self.UrlCategories.url_categories.keys():
                self.configs[device_group].update({'objects': {'url-categories':
                            {'entry': self.UrlCategories.url_categories }}})

    def commit_all(self, device_group: str) -> Dict[str,Any]:
        """Specific Device group commit."""
        resp = commit_panorama_device_group(device=self.device,api_key=self.api_key,
                    device_group=device_group,verify=self.certstore)
        return resp

    @property
    def url_search(self):
        raise PaloAltoAPIError(f"{self.__class__} cannot search url")
