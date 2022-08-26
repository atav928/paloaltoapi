"""Baseline Firewall Class"""

import sys
from typing import Any, Dict, List
from bs4 import BeautifulSoup as BS
from requests.exceptions import HTTPError
from paloaltoapi import config

from paloaltoapi.commit import check_job, commit_config, commit_lock, commit_revert
from paloaltoapi.highavail import HighAvail
from paloaltoapi.url_search.urlsearch import check_url_category
from paloaltoapi.utils import format_resp
from paloaltoapi.xmlparser import xml2dict
from paloaltoapi.statics import FW_ATTR, PARSER
from paloaltoapi.exceptions import PaloAltoAPIError, CredentialsError
from paloaltoapi.urls import ApiCalls, Url
from paloaltoapi.tags.dynamic_tags import AutoTags
from paloaltoapi.paloalto import paloalto_system

class Firewall:
    """Palo Alto baseline Device"""
    def __init__(self, device, username=None, passwd=None,
                certstore=None, key=None):
        for i in FW_ATTR:
            setattr(self, i, None)
        self.device = device
        self.version = None
        self.certstore = certstore if certstore is not None else config.CERT
        self.api_key = key if key else self.get_key(username, passwd, update=False)
        self.system = None
        self.high_avail_status()
        self.get_version()
        #self.system = paloalto_system(self.get_version())

    def __str__(self):
        return self.device

    def __repr__(self):
        # Change: attrs = str([x for x in self.__dict__])
        return "<paloaltoapi.firewall.Firewall: {}> {} ".format(
            str(self), str(list(self.__dict__)))

    def get_key(self, username, password, update=True):
        """Generate Key"""
        if not username or not password:
            raise CredentialsError
        values = Url.key_gen(self.device,username,password)
        #r = self.request_get(url=values['url'], params=values.get('params', None),
        res = ApiCalls.request(url=values['url'], req_type=values['request_type'],
                    params=values.get('params', None),
                    headers=values.get('headers', None),
                    data=values.get('data', None),
                    verify=self.certstore)
        soup = BS(res.text, features=PARSER)
        if res.status_code == 200:
            if update:
                self.key = soup.find('key').text
            return soup.find('key').text
        else:
            raise HTTPError(soup.find('msg').text)

    def get_version(self):
        """Retreive Version"""
        values = Url.get_version(self.device, self.api_key)
        res = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                            params=values.get('params', None),
                            headers=values.get('headers', None),
                            data=values.get('data', None),
                            verify=self.certstore)
        soup = BS(res.text, features='html.parser')
        try:
            #print(soup)
            xmldict = xml2dict(str(soup))
            #print(xmldict)
            self.sw_version = xmldict['result']['system'].get('sw-version', None)
            try:
                self.version = '.'.join(self.sw_version.split('.')[:2])
            except KeyError as err:
                raise PaloAltoAPIError(
                    f"Unable to retrive version from sw_version={self.sw_version} error={err}"
                    )
            self.uptime = xmldict['result']['system'].get('uptime', None)
            self.device_certificate = xmldict['result']['system'].get(
                'device-certificate-status', None)
            self.hostname = xmldict['result']['system'].get('hostname', None)
            self.devicename = xmldict['result']['system'].get('devicename', None)
            self.model = xmldict['result']['system'].get('model', None)
            self.serial = xmldict['result']['system'].get('serial', None)
            self.ip_address = xmldict['result']['system'].get('ip-address', None)
            self.default_gateway = xmldict['result']['system'].get('default-gateway', None)
            self.time = xmldict['result']['system'].get('time', None)
            self.system = paloalto_system(xmldict['result']['system'])
            return xmldict['result']['system']
        except AttributeError as err:
            raise PaloAltoAPIError from err

    def high_avail_status(self):
        """Get High Avail Status"""
        # TODO: move this clal over to the High Avail section to handle
        values = Url.xml_ha_get_status(self.device, self.api_key)
        res = ApiCalls.request(req_type='GET',url=values['url'],
                                params=values.get('params', None),
                                headers=values.get('headers', None),
                                verify=self.certstore)
        soup = BS(res.text, features='html.parser')
        try:
            #print(soup)
            xmldict = xml2dict(str(soup))
            #print(xmldict)
            self.high_avail = HighAvail(xmldict, self.device, self.api_key,
                                        is_panorama=False)
        except AttributeError as err:
            raise PaloAltoAPIError(err)
        except TypeError as err:
            sys.exit(err)

    def __check_if_autotags(self):
        try:
            getattr(self, "AutoTags")
        except AttributeError:
            self.AutoTags = AutoTags(device=self.device, api_key=self.api_key,
                                    certstore=self.certstore)

    def autotags(self):
        """Checks if autotag exists callable from outside"""
        self.__check_if_autotags()

    def get_dynamic_tags(self, name: str = 'all'):
        """Get dynamic tags"""
        # changed: try:
        # changed:    getattr(self, "AutoTags")
        # changed: except AttributeError:
        # changed:     self.AutoTags = AutoTags(
        # changed: device=self.device, api_key=self.api_key,
        # changed:                             certstore=self.certstore)
        self.__check_if_autotags()
        self.AutoTags.get_dynamic_tags(name=name)

    def get_registered_ip_list(self, name: str) -> None:
        """Get Registered IP from TAG

        Args:
            name (str): Name of DAG, required
        """
        self.__check_if_autotags()
        self.AutoTags.get_registered_ip(tag=name)

    def commit(self) -> Dict[str,Any]:
        """Commit candidate configs to the firewall"""
        resp = commit_config(self.device,self.api_key,verify=self.certstore)
        result = format_resp(resp)
        return result

    def check_jobid(self, jobid: str) -> Dict[str,Any]:
        """Check Status of Job"""
        resp = check_job(self.device,self.api_key,jobid=jobid,verify=self.certstore)
        result = format_resp(resp)
        return result

    def add_commit_lock(self, comment: str = 'paloaltoapi') -> Dict:
        """Adds a commit lock for current user"""
        return commit_lock(commit_type='add', comment=comment,
                        api_key=self.api_key,device=self.device,verify=self.certstore)

    def show_commit_lock(self) -> Dict:
        """Shows current commit locks"""
        return commit_lock(commit_type='show',api_key=self.api_key,device=self.device,
                        verify=self.certstore)

    def remove_commit_lock(self, admin: str = None) -> Dict:
        """Removes Commit Lock
        :params admin: If supplied removes a specific Lock
        """
        return commit_lock(commit_type='remove',admin=admin,api_key=self.api_key,
                        device=self.device,verify=self.certstore)

    def revert_changes(self, admin: str = None) -> Dict:
        """Revert Changes pending commit.

        Args:
            admin (str, optional): Specifies a username specific changes to revert.
             Defaults to None.

        Returns:
            Dict: Palo Alto Response
        """
        return commit_revert(admin=admin,device=self.device,
                            api_key=self.api_key,verify=self.certstore)

    def url_search(self, url: str, search_type: str = 'url') -> List[str]:
        """Returns the current category for a specified URL.
         Two search types exist depending on the database looking to query.

        Args:
            url (str): URL to search in an FQDN format
            search_type (str, optional): Which database to search 'url' or 'custom-url'.
             Defaults to 'url'.

        Returns:
            List[str]: Returns list of categories that URL belongs to
        """
        return check_url_category(self.device,self.api_key,url=url,search_type=search_type)
