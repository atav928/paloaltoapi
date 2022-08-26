"""Shared Object Configs"""

import json
from typing import Any, Dict, List
from collections import OrderedDict
from paloaltoapi import config
from paloaltoapi.urls import ApiCalls, create_url_base, define_params

from paloaltoapi.utils import xml_call
from paloaltoapi.exceptions import PaloAltoAPIError, PaloAltoMissingParam, ParamsError

def _address_xml_search(search_params: list, obj: str, **kwargs) -> OrderedDict:
    """Searches for address using XML"""
    device = kwargs.get('device')
    certstore = kwargs.get('certstore')
    api_key = kwargs.get('api_key')
    if not device or not api_key:
        raise ParamsError('device=None, api_key=None')
    for search in search_params:
        entry = xml_call(device=device, xpath=search['xpath'].format(obj),
                         certstore=certstore, api_key=api_key)
        if entry['result']:
            break
    return entry

def _address_grp_xml_search(search_params: list, obj: str, **kwargs) -> OrderedDict:
    """Searches for address using XML does not supply locations"""
    device = kwargs.get('device')
    certstore = kwargs.get('certstore')
    api_key = kwargs.get('api_key')
    addrgrp_member_list = []
    if not device or not api_key:
        raise ParamsError('device=None, api_key=None')
    for search in search_params:
        entry = xml_call(device=device, xpath=search['xpath'].format(obj),
                         certstore=certstore, api_key=api_key)
        tmp = _extract_address_group(entry)
        addrgrp_member_list = addrgrp_member_list + tmp
    #print(f'{addrgrp_member_list=}')
    addrgrp_member_list = list(set(addrgrp_member_list))
    return addrgrp_member_list

def _extract_address(entry: OrderedDict) -> str:
    """
    Extracts Address Value from XML Return
    """
    # Checks if there is a result
    if entry['result']:
        # Sets the first entry results to a value to parse
        value = entry['result']['entry']
        if value.get('ip-netmask'):
            addr_value = value.get('ip-netmask')
        elif value.get('fqdn'):
            addr_value = value.get('fqdn')
        else:
            addr_value = None
    # Defaults to None
    else:
        addr_value = None
    return addr_value

def _tags_xml_search(search_params: List, obj: str, **kwargs) -> Dict[str, Any]:
    """Extract tags"""

    device = kwargs.get('device')
    certstore = kwargs.get('certstore')
    api_key = kwargs.get('api_key')
    if not device or not api_key:
        raise ParamsError('device=None, api_key=None')
    for search in search_params:
        entry = xml_call(device=device, xpath=search['xpath'].format(obj),
                         certstore=certstore, api_key=api_key)
        if entry['result']:
            entry['result']['location-type'] = search['location-type']
            break
    entry = json.dumps(entry)
    entry = json.loads(entry)
    return entry['result']

def _extract_address_group(entry: OrderedDict) -> List[str]:
    """
    Extracts Address Value from XML Return
    """
    # convert OrderedDict to dict
    entry = json.loads(json.dumps(entry))
    #print(f'{entry=}')
    entries_exist = False
    count = 0
    # Defaults to None
    addr_value = []
    try:
        if entry['result']:
            count = int(entry['result']['@total-count'])
            entries_exist = True
        # Case only 1 list of values
        if entries_exist and count == 1:
            if isinstance(entry['result']['entry']['static']['member'], str):
                addr_value.append(entry['result']['entry']['static']['member'])
                #print(f'{addr_value=}')
            else:
                addr_value = entry['result']['entry']['static']['member']
                #print(f"{addr_value=}")
        # Case multiple values in different groups
        if entries_exist and count > 1:
            addr_value = []
            for entry_list in entry['result']['entry']:
                if isinstance(entry_list['static']['member'], str):
                    addr_value.append(entry_list['static']['member'])
                    #print(f'{addr_value=}')
                else:
                    addr_value = addr_value + entry_list['static']['member']
                    #print(f'{addr_value=}')
            addr_value = list(set(addr_value))
    except (TypeError,KeyError) as err:
        raise PaloAltoAPIError from err
    #print(f'{addr_value=}')
    return addr_value

def create_address_data(kwargs:dict):
    """Create data payload for address obj"""
    # Build Payload
    data = {}
    data = {'entry': [{}]}
    values = data['entry'][0]
    values['@name'] = kwargs['address_name']
    if kwargs['location'] != 'shared':
        values['@location'] = kwargs['location']
    if kwargs.get('ip_netmask'):
        values['ip-netmask'] = kwargs['ip_netmask']
    if kwargs.get('fqdn'):
        values['fqdn'] = kwargs['fqdn']
    if kwargs.get('tag') and isinstance(kwargs.get('tag'), list):
        values['tag'] = {'member': kwargs['tag']}
    if kwargs.get('description'):
        values['description'] = kwargs['description']
    return data

def delete_address(**kwargs) -> Dict[str, Any]:
    """Deletes an Address Object using Palo Alto RestAPI
    :param device:
    :param api_key:
    :param version:
    :param name:
    :param location:
    """
    try:
        device=kwargs['device']
        api_key=kwargs['api_key']
        version=kwargs['version']
        address_name=kwargs['name']
        verify=kwargs.get('verify', None)
        location=kwargs.get('location') if kwargs.get('location') else 'shared'
    except KeyError as err:
        raise PaloAltoMissingParam(err)
    params = define_params(location,address_name)
    url = create_url_base(device, version)
    url = url + config.REST_URLS['addresses']
    method ='DELETE'
    headers = {
        "X-PAN-KEY": api_key
    }
    resp = ApiCalls.request(url=url,req_type=method,params=params,
                            headers=headers,verify=verify)
    response = resp.json()
    response['error'] = bool(resp.status_code != 200)
    return response

def create_address(address_name: str, location: str, version: str,
                    device:str, api_key: str, data: Dict[str, Any],certstore = None):
    """Creates a address object"""
    params = define_params(location, address_name)
    url = create_url_base(device, version)
    url = url + config.REST_URLS['addresses']
    method='POST'
    headers = {
        "X-PAN-KEY": api_key,
    }
    resp = ApiCalls.request(url=url, req_type=method,params=params, headers=headers,
                            verify=certstore, data=data)
    response = resp.json()
    response['error'] = bool(resp.status_code != 200)
    return response

def create_address_grp_data(kwargs: dict):
    """Create data payload for address obj"""
    # Build Payload
    data = {}
    data = {'entry': [{}]}
    values = data['entry'][0]
    values['@name'] = kwargs['address_grp']
    values['static'] = {'member': kwargs['address_members']}
    if kwargs['location'] != 'shared':
        values['@location'] = kwargs['location']
    if kwargs.get('tag') and isinstance(kwargs.get('tag'), list):
        values['tag'] = {'member': kwargs['tag']}
    if kwargs.get('description'):
        values['description'] = kwargs['description']
    return data

def list_address_grp(address_name: str, location: str, version: str,
                    device: str, api_key: str, certstore = None):
    """Creates a address Group Object"""
    params = define_params(location, address_name)
    url = create_url_base(device, version)
    url = url + config.REST_URLS['address_groups']
    method='GET'
    headers = {
        "X-PAN-KEY": api_key,
    }
    resp = ApiCalls.request(url=url, req_type=method,params=params, headers=headers,
                            verify=certstore)
    return resp.json()

def create_address_grp(address_name: str, location: str, version: str,
                    device:str, api_key: str, data: Dict[str, Any],certstore = None):
    """Creates a address Group Object"""
    params = define_params(location, address_name)
    url = create_url_base(device, version)
    url = url + config.REST_URLS['address_groups']
    method='POST'
    headers = {
        "X-PAN-KEY": api_key,
    }
    resp = ApiCalls.request(url=url, req_type=method,params=params, headers=headers,
                            verify=certstore, data=data)
    # TODO: Testing out how the response needs to be handled
    response = resp.json()
    response['error'] = bool(resp.status_code != '200')
    return response

def update_address_grp(address_name: str, location: str, version: str,
                    device:str, api_key: str, data: Dict[str, Any],certstore = None):
    """Creates a address Group Object"""
    params = define_params(location, address_name)
    url = create_url_base(device, version)
    url = url + config.REST_URLS['address_groups']
    method='PUT'
    headers = {
        "X-PAN-KEY": api_key,
    }
    resp = ApiCalls.request(url=url, req_type=method,params=params, headers=headers,
                            verify=certstore, data=data)
    # TODO: Testing out how the response needs to be handled
    response = resp.json()
    response['error'] = bool(resp.status_code != '200')
    return response
