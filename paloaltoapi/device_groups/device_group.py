# pylint: disable=line-too-long
"""Device Gruop"""

import threading

from paloaltoapi.exceptions import PaloAltoAPIError
from paloaltoapi.firewall import Firewall
from paloaltoapi.statics import DEVICEGROUP_ATTR
from paloaltoapi.urls import Url, ApiCalls


class DeviceGroup(Firewall):
    """
    Creates a Device Group
    """

    def __init__(self, device_list: list, device: str, key: str, certstore=None):
        """
        Init
        """
        super().__init__(device=device, certstore=certstore, key=key)
        self.device = device
        self.api_key = key
        self.certstore = certstore if certstore is not None else False
        # no longer needed since handled Panorama module. May need to add
        # checks to ensure it exists here though.
        # self.device_list = device_list.append('shared') if 'shared' not in device_list
        # else device_list
        self.device_list = device_list
        # print(self.device_list)
        # Create an internal dictionary of all the rules to export
        self.device_group = {devgrp: {"policy": {'security': {
            "pre-rules": {"entry": []}, "post-rules": {"entry":
                                                       []}}}} for devgrp in self.device_list}
        # Create a map function to correlate new name with the actual device-group name
        # use to check before needing to pull data from Panorama
        # self.device_group_map = {devgrp.replace(
        #    '-', '_'): devgrp for devgrp in self.device_list}
        self.device_group_map = {devgrp:
                                 devgrp.replace('-', '_') for devgrp in self.device_list}
        # for i in device_list:
        for i in self.device_group_map.values():
            setattr(self, i, {k: None for k in DEVICEGROUP_ATTR})
        self.get_security_rules()

    def __str__(self):
        return self.device

    def __repr__(self):
        return "<paloaltoapi.device_groups.device_group.DeviceGroup: {}> {} ".format(
            str(self), str(list(self.__dict__)))

    def get_security_rules(self, device: list = None):
        """Retrieve rules from each group"""
        device = device if device else ['all']

        if 'all' in device:
            device_group = self.device_list
        else:
            device_group = [i for i in device if i in self.device_list]

        if not device_group:
            raise PaloAltoAPIError("Cannot process an empty device group")

        for devgrp in device_group:
            params = {}
            params['device_group'] = devgrp
            params['api_key'] = self.api_key
            params['device'] = self.device
            params['certstore'] = self.certstore
            params['version'] = self.version

            threads = []
            thr = threading.Thread(target=thread_function, args=(params, self.device_group))
            threads.append(thr)
            thr.start()
        for index, thread in enumerate(threads):
            #print("Main    : before joining thread %d.", index)
            thread.join()
            #pbar.update(count)
            #count += 1

    def update_objects(self):
        """update object"""
        for devgrp in self.device_group.keys():
            if getattr(self, devgrp):
                pass


def thread_function(params: dict, results: dict):
    """Threads Firewall Policy retrival

    Args:
        firewall (str): _description_
        username (str): _description_
        password (str): _description_
        results (dict): _description_
    """
    #print("Thread %s: starting", params['device'])
    # Gather Pre-Rules
    values = Url.restapi_policy_getprerule(
        params['device'], params['api_key'], version=params['version'], device_group=params['device_group'])
    res = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                           params=values.get('params', None),
                           headers=values.get('headers', None),
                           data=values.get('data', None),
                           verify=params['certstore'])
    jsondata = res.json()
    #print(f"{params['device_group']}: {jsondata}")
    if jsondata['@status'] != 'success':
        raise PaloAltoAPIError(
            "Unable to retrieve rules for {} response: {}".format(params['device_group'], jsondata))
    if int(jsondata['result']['@total-count']) > 0:
        try:
            results[params['device_group']
                    ]['policy']['security']['pre-rules']['entry'] = jsondata['result'].get('entry', None)
        except (KeyError, TypeError) as err:
            raise PaloAltoAPIError(
                "Trying to get post-rulebase for {} got {}".format(params['device_group'], err))
    # Gather Post-Rules
    values = Url.restapi_policy_getpostrule(
        params['device'], params['api_key'], version=params['version'], device_group=params['device_group'])
    res = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                           params=values.get('params', None),
                           headers=values.get('headers', None),
                           data=values.get('data', None),
                           verify=params['certstore'])
    jsondata = res.json()
    if jsondata['@status'] != 'success':
        raise PaloAltoAPIError(
            "Unable to retrieve rules for {} response: {}".format(params['device_group'], jsondata))
    if int(jsondata['result']['@total-count']) > 0:
        try:
            results[params['device_group']
                    ]['policy']['security']['post-rules']['entry'] = jsondata['result'].get('entry', None)
            #print(f"results: {results}")
        except (KeyError, TypeError) as err:
            raise PaloAltoAPIError(
                "Trying to get post-rulebase for {} got {}".format(params['device_group'], err))
