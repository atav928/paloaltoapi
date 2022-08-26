"""Commit Actions"""

from collections import OrderedDict
from typing import Dict
from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoAPIError, PaloAltoMissingParam
from paloaltoapi.utils import format_resp, xml_call

def set_audit_comment(**kwargs) -> OrderedDict:
    """Sets the audit comment in a rule; cannot commit if changes to a rule
    were made and an Audit was not added.
    :params rule:
    :params device:
    :params api_key:
    :params rulebase:
    :params verify:
    :params change_num:
    :params rule_type: Default security; used to specify the type of rule
    """
    try:
        location=kwargs['location']
        rulebase = kwargs['rulebase']
        rulename = kwargs['rule']
        device = kwargs['device']
        api_key = kwargs['api_key']
        change_num = kwargs['change_num']
        rule_type = kwargs.get('rule_type', 'security')
    except KeyError as err:
        raise PaloAltoMissingParam(err)
    if rule_type not in ['security']:
        raise PaloAltoAPIError(f'rule_type={rule_type}')
    if location == 'shared':
        xpath = config.POLICIES['audit']['shared'].format(rulebase,rule_type,rulename)
    else:
        xpath = config.POLICIES['audit']['device-group'].format(location,rulebase,
                                                                rule_type,rulename)
    params = {'cmd': config.POLICIES['audit']['cmd'].format(xpath,change_num)}
    resp = xml_call(device,xpath,api_key,action=None,param_type='op',params=params)
    result = format_resp(resp)
    return result

def commit_config(device: str, api_key: str, verify = None):
    """
    Commit— Commit candidate changes to the firewall.
    """
    params = {'cmd': config.COMMANDS['panorama_commit']}
    resp = xml_call(device=device,xpath=None,api_key=api_key,
                    action=None,param_type='commit',params=params,
                    certstore=verify)
    return resp

def check_job(device: str, api_key: str, jobid: str, verify=None, **kwargs):
    """
    Checks on Panorama JobID. Used for Async requests
    """
    params = {'cmd': config.COMMANDS['get_job'].format(jobid)}
    resp = xml_call(device=device,xpath=None,api_key=api_key,action='get',
                    certstore=verify,params=params,param_type='op')
    result = format_resp(resp)
    return result

def commit_panorama_device_group(device: str, api_key: str, device_group: str,
                                verify=None,**kwargs):
    """
    Commit Push for a local config
    """
    params = {'cmd': config.COMMANDS['device_commit'].format(device_group)}
    resp = xml_call(device=device,xpath=None,api_key=api_key,action='all',
                certstore=verify,params=params,param_type='commit')
    result = format_resp(resp)
    return result

def commit_lock(commit_type: str='show',comment: str='Automation', **kwargs):
    """Gets a commit log"""
    if commit_type == 'show':
        params = {'cmd': config.COMMANDS['commit_lock']['show']}
    elif commit_type in ['add','set']:
        params = {'cmd': config.COMMANDS['commit_lock']['add'].format(comment)}
    elif commit_type == 'remove':
        cmd = (config.COMMANDS['commit_lock']['remove']
                if not kwargs.get('admin') else
                    config.COMMANDS['commit_lock']['remove_admin'].format(kwargs['admin']))
        params = {'cmd': cmd}
    else:
        raise PaloAltoAPIError(commit_type)
    resp = xml_call(kwargs['device'],xpath=None,api_key=kwargs['api_key'],action=None,
                    param_type='op',params=params)
    return format_resp(resp)

def commit_revert(admin: str = None, **kwargs) -> Dict:
    """Reverts configurations prior to being commited to 

    Args:
        admin (str, optional): [description]. Defaults to None.

    Returns:
        Dict: [description]
    """
    if admin:
        params = {'cmd': config.COMMANDS['commit_revert']['admin'].format(admin)}
    else:
        params = {'cmd': config.COMMANDS['commit_revert']['all']}
    resp = xml_call(kwargs['device'],xpath=None,api_key=kwargs['api_key'],action=None,
                    param_type='op',params=params)
    return format_resp(resp)
