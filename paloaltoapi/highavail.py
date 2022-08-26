from dataclasses import dataclass
from xml.etree import cElementTree as ElementTree
from bs4 import BeautifulSoup as BS
from requests.models import Response
from paloaltoapi.exceptions import PaloAltoAPIError
from paloaltoapi.xmlparser import XmlDictConfig, xml2dict
from paloaltoapi.urls import Url, ApiCalls
from paloaltoapi.statics import HA_ATTR

## Trying to build out composition class structure still working on 
class HighAvail:
    def __init__(self, response, device, key, certstore=None,
                is_panorama: bool = False):
        self.device = device
        self.api_key  = key
        self.certstore = certstore if certstore != None else False
        self._is_panorama = is_panorama
        for i in HA_ATTR:
            setattr(self, i, None)
        self.update(response)

    def __str__(self):
        return self.device
    
    def __repr__(self):
        attrs = str([x for x in self.__dict__])
        return "<paloaltoapi.highavail.HighAvail: {}> {} ".format(str(self), attrs)

    def update(self, response):
        """Dictionary format; please use xml2dict with XML response"""
        #if is_panorama:
        #    self.ha_attributes = HA_PANORAMA(response)
        #    for i in HA_ATTR:
        #        setattr(self, i, self.ha_attributes[i])
        #if not is_panorama:
        #    self.ha_attributes = HA_FIREWALL(response)
        #    for i in HA_ATTR:
        #        setattr(self, i, self.ha_attributes[i])
        # TODO: Build out a data class to simplify this
        if self._is_panorama:
            self.ha_enabled = response['result'].get('enabled', None)
                
            if self.ha_enabled == 'yes':
                self.ha_running_sync = response['result'].get('running-sync-enabled', None)
                self.ha_local_priority = response['result']['local-info'].get('priority', None)
                self.ha_local_state = response['result']['local-info'].get('state', None)
                self.ha_local_preemptive = response['result']['local-info'].get('preemptive', None)
                self.ha_local_sync_running = response['result'].get('running-sync', None)
                self.ha_local_sync_enabled = response['result'].get('running-sync-enabled', None)
                self.ha_peer_ip = response['result']['peer-info'].get('mgmt-ip', None)
                self.ha_peer_state = response['result']['peer-info'].get('state', None)
        else:
            # TODO: build out the Firewall HA response properly
            self.ha_enabled = response['result'].get('enabled', None)

    def high_avail_update(self):
        values = Url.xml_ha_get_status(self.device, self.api_key)
        r = ApiCalls.request(req_type=values['request_type'], 
                            url=values['url'], 
                            params=values.get('params', None),
                            data=values.get('data', None),
                            headers=values.get('headers', None))
        soup = BS(r.text, features='html.parser')
        try:
            xmldict = xml2dict(str(soup))
            self.update(xmldict)
        except AttributeError as err:
            raise PaloAltoAPIError(err)    

    def high_avail_suspend(self):
        values = Url.xml_ha_suspend(self.device, self.api_key)
        r = ApiCalls.request_get(url=values['url'], 
                            params=values.get('params', None),
                            headers=values.get('headers', None), 
                            verify=self.certstore)
        soup = BS(r.text, features='html.parser')
        try:
            xmldict = xml2dict(str(soup))
            self.ha_suspend_state = True if xmldict.get('status', None) == 'success' else False
            # update values
            self.high_avail_update()
        except AttributeError as err:
            raise PaloAltoAPIError(err) 
             
    def high_avail_functional(self):
        values = Url.xml_ha_functional(self.device, self.api_key)
        r = ApiCalls.request_get(url=values['url'], params=values.get('params', None),
                            headers=values.get('headers', None), verify=self.certstore)
        soup = BS(r.text, features='html.parser')
        try:
            xmldict = xml2dict(str(soup))
            self.ha_suspend_state = False if xmldict.get('status', None) == 'success' else self.ha_suspend_state
            # update values
            self.high_avail_update()
        except AttributeError as err:
            raise PaloAltoAPIError(err)  


@dataclass
class HA_PANORAMA:
    def __init__(self, response: dict):
        self.ha_enabled = response['result'].get('enabled', None)
            
        if self.ha_enabled == 'yes':
            self.ha_running_sync = response['result'].get('running-sync-enabled', None)
            self.ha_local_priority = response['result']['local-info'].get('priority', None)
            self.ha_local_state = response['result']['local-info'].get('state', None)
            self.ha_local_preemptive = response['result']['local-info'].get('preemptive', None)
            self.ha_local_sync_running = response['result'].get('running-sync', None)
            self.ha_local_sync_enabled = response['result'].get('running-sync-enabled', None)
            self.ha_peer_ip = response['result']['peer-info'].get('mgmt-ip', None)
            self.ha_peer_state = response['result']['peer-info'].get('state', None)

@dataclass
class HA_FIREWALL:
    def __init__(self, response: dict):
        self.ha_enabled = response['result'].get('enabled', None)
            
        if self.ha_enabled == 'yes':
            self.ha_running_sync = response['result'].get('running-sync-enabled', None)
            self.ha_local_priority = response['result']['local-info'].get('priority', None)
            self.ha_local_state = response['result']['local-info'].get('state', None)
            self.ha_local_preemptive = response['result']['local-info'].get('preemptive', None)
            self.ha_local_sync_running = response['result'].get('running-sync', None)
            self.ha_local_sync_enabled = response['result'].get('running-sync-enabled', None)
            self.ha_peer_ip = response['result']['peer-info'].get('mgmt-ip', None)
            self.ha_peer_state = response['result']['peer-info'].get('state', None)    