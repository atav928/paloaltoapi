"""Palo Alto Shared Utilities"""
from collections import OrderedDict
import json
from typing import Dict
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup as BS
import requests
import xmltodict

from paloaltoapi import config
from paloaltoapi.xmlparser import xml2dict
from paloaltoapi.urls import Url, ApiCalls
from paloaltoapi.exceptions import PaloAltoAPIError

def define_certstore(certstore):
    """Defines how certstore is handled as it passes"""
    return certstore if certstore is not None else config.CERT

def get_version(device: str, api_key: str, certstore = None) -> str:
    """Retrieves PA Device Version
    """
    values = Url.get_version(device, api_key)
    res = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                        params=values.get('params', None),
                        headers=values.get('headers', None),
                        data=values.get('data', None),
                        verify=certstore)
    soup = BS(res.text, features='html.parser')
    try:
        #print(soup)
        xmldict = xml2dict(str(soup))
        #print(xmldict)
        sw_version = xmldict['result']['system'].get('sw-version', None)
        try:
            version = '.'.join(sw_version.split('.')[:2])
            return version
        except KeyError as err:
            raise PaloAltoAPIError(
                f"Unable to retrive version from sw_version={sw_version} error={err}"
                )
    except AttributeError as err:
        raise PaloAltoAPIError from err


def xml_call(device: str, xpath: str, api_key: str,action: str = 'get',
               certstore = None, **kwargs) -> OrderedDict:
    """
    :param device: Firewall endpoint in FQDN form
    :type device: str
    :param xpath: XPATH param for XML call
    :type xpath: str
    :param api_key: Palo Alto API Key
    :type api_key: str
    :param action: XML API call Action Type default 'get'
    :type action: str
    :param param_type: Default 'config'
    :return: Palo Alto Response from requests library
    :rtype: dict
    """
    param_type = kwargs.get('param_type','config')
    certstore = certstore if certstore is not None else config.CERT
    params = {
        "type": param_type,
        "action": action,
        "xpath": xpath
    }
    # Adds additional params like element field if needed in XML query
    if kwargs and 'params' in kwargs.keys():
        params = {**params, **kwargs['params']}
    headers = {
        'X-PAN-KEY': api_key
    }
    url = f"https://{device}/api/"
    # Allow a method to be passed to chagne the API Call defaults to POST
    method=kwargs.get('method', "POST")
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

def format_resp(response: OrderedDict) -> Dict:
    """Format a Ordered Dict response"""
    resp = json.loads(json.dumps(response))
    # remove @
    resp = {key.split('@')[-1]: value for key,value in resp.items()}
    return resp

def format_panos_resp(response: ET) -> OrderedDict:
    """Reformats a xml response from pan-os-python package into a json response

    Args:
        response (ET): xml.etree.ElementTree required to parse

    Returns:
        OrderedDict: Response Ordered dict
    """
    return xmltodict.parse(
        ET.tostring(response,encoding='utf8', method='xml'))
