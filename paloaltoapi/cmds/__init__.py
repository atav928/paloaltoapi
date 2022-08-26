"""Utilities for CMDS"""
import json
import re
import requests
import xmltodict

from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoAPIError
from paloaltoapi.utils import define_certstore


class SensitiveFormatter:
    """Formatter that removes sensitive information in urls."""
    @staticmethod
    def _filter(sen):
        return re.sub(r'key=[^&]*', r'key=********', sen)

    def format(self, record):
        """Reformats error message extracting key

        Args:
            record ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self._filter(record)

def xml_cmd_call(device: str, cmd: str, api_key: str,
               certstore = None) -> dict:
    """
    :param xpath: XPATH param for XML call
    :type xpath: str
    :return: Palo Alto Response from requests library
    :rtype: dict
    """
    certstore = define_certstore(certstore)
    params = {
        "type": "op",
        "cmd": cmd,
        "key": api_key
    }
    url = f"https://{device}/api/"
    method="POST"
    try:
        res = requests.request(
            url=url,
            method=method,
            params=params,
            verify=certstore
        )
        #print(res.json())
        res.raise_for_status()
        # removed: print(xmltodict.parse(res.text)["response"])
    except Exception as err:
        err = SensitiveFormatter().format(str(err))
        raise Exception(err)
    result = json.dumps(xmltodict.parse(res.text)["response"])
    result = json.loads(result)
    return result
