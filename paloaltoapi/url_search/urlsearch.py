"""URL Search"""
import re

from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoAPIError
from paloaltoapi.utils import xml_call


def check_url_category(device: str, api_key: str, url: str, search_type: str = 'url', verify=False):
    """Function that handles URL Category Searches

    Args:
        device (str): Firewall Device
        api_key (str): Firewall API Key
        url (str): URL to serach (FQDN format)
        search_type (str, optional): 'url' or 'custom-url'. Defaults to 'url'.
        verify (bool, optional): Certificate Verification. Defaults to False.

    Raises:
        PaloAltoAPIError: [description]

    Returns:
        [type]: [description]
    """
    if search_type not in ['url', 'custom-url']:
        raise PaloAltoAPIError(f'unsupported search_type={search_type}')
    params = {'cmd': config.URL_SEARCHES[search_type].format(url)}
    resp = xml_call(
        device,
        xpath=None,
        params=params,
        api_key=api_key,
        certstore=verify,
        param_type='op')
    if search_type == 'url':
        raw_list = resp['result'].split('\n')[-1]
        category_list = raw_list.split(' ')[1:-2]
        if len(category_list) == 0:
            raise PaloAltoAPIError(f'no results {resp=}')
    if search_type == 'custom-url':
        category_list = [cat.strip() for cat in resp['result'].split('\n')[1:]]
    return category_list
