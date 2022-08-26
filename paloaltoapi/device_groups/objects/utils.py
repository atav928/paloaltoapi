"""Object Utilities"""
from collections import OrderedDict
from typing import Dict
from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoTaskError
from paloaltoapi.utils import xml_call

def add_obj_to_address_group(**kwargs) -> OrderedDict:
    """Adds an Obj to an Address Group. Supports only 'shared' location type.
    Required Params
    --------
    :param api_key:
    :type api_key: str
    :param device:
    :type device: str
    :param member: object to add
    :type member: str
    Optional Params
    --------
    :param location: if not Shared than must be a valid Device Group
    :type location: str
    :param verify: certificate verification
    :type verify: str | bool
    Return
    ----
    :description: returns response from Palo alto
    :rtype: OrderedDict"""
    try:
        api_key = kwargs['token']
        device = kwargs['device']
        location = kwargs['location']
        address_group = kwargs['address_group']
        member = kwargs['member']
        verify = kwargs.get('verify', False)
    except KeyError as err:
        raise err
    if location.lower() == 'shared':
        xpath = config.ADDRESS_GROUP['add']['shared'].format(address_group)
    else:
        raise PaloAltoTaskError('device-group')
    params = {'element': config.ADDRESS_GROUP['element'].format(member)}
    resp = xml_call(device=device,api_key=api_key, xpath=xpath,
                    certstore=verify, action='set', params=params)
    result = {'response': return_response(resp, action='add',member=member,
                        group=address_group,location=location)}
    return result

def delete_obj_from_address_group(**kwargs) -> Dict[str,str]:
    """Deletes an Obj to an Address Group. Supports only 'shared' location type.
    Required Params
    --------
    :param api_key:
    :type api_key: str
    :param device:
    :type device: str
    :param member: object to add
    :type member: str
    Optional Params
    --------
    :param location: if not Shared than must be a valid Device Group
    :type location: str
    :param verify: certificate verification
    :type verify: str | bool
    Return
    ----
    :description: returns response from Palo alto
    :rtype: OrderedDict"""
    action = 'delete'
    try:
        api_key = kwargs['token']
        device = kwargs['device']
        location = kwargs['location']
        address_group = kwargs['address_group']
        member = kwargs['member']
        verify = kwargs.get('verify', False)
    except KeyError as err:
        raise err
    if location.lower() == 'shared':
        xpath = config.ADDRESS_GROUP['update']['shared'].format(address_group, member)
    else:
        raise PaloAltoTaskError('device-group')
    resp = xml_call(device=device,api_key=api_key, xpath=xpath,
                    certstore=verify, action=action)
    result = {'response': return_response(resp, action=action,member=member,
                                        group=address_group,location=location)}
    return result

def return_response(message: OrderedDict, action: str, member: str, group: str, location: str) -> Dict[str,str]:
    """reformats the response"""
    result_list =['status','message','member','address_group','location']
    result = {r: None for r in result_list}
    result['status'] = message['@status']
    result['action'] = action
    result['member'] = member
    result['address_group'] = group
    result['location'] = location
    result['message'] = message['msg']
    return result
