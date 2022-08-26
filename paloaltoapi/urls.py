"""URLS File"""
import json
from typing import Any, Dict, List
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError, SSLError
from requests.models import Response
import requests
from requests.packages import urllib3
from bs4 import BeautifulSoup as BS
from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoAPIError, ParamsError
from paloaltoapi.xmlparser import xml2dict
from paloaltoapi.tags.tags_forms import xml_unregister_tag, xml_register_tag
from paloaltoapi.statics import BASEURL

urllib3.disable_warnings()

def reformat_xml(raw_text: Response):
    """
    Reformats XML response
    """
    soup = BS(raw_text.text, features='html.parser')
    return xml2dict(str(soup))

def define_params(location='shared', name=None):
    """
    Fills sttnadard Palo Alto Parameters that are used to fill RestAPI Params
    Params
    ======
    location: str\n
        \tdefault 'shared'; used to set the location of an Object\n
    name: str\n
        \tUsed to specify a named object to access.
    """
    if not name and location == 'shared':
        # params = (
        return (
            ('location', location),
            ('input-format', 'json'),
            ('output-format', 'json')
        )
    elif name and location == 'shared':
        # params = (
        return (
            ('location', 'shared'),
            ('name', name),
            ('input-format', 'json'),
            ('output-format', 'json')
        )
    elif name and location != 'shared':
        # params = (
        return (
            ('location', 'device-group'),
            ('name', name),
            ('device-group', location),
            ('input-format', 'json'),
            ('output-format', 'json')
        )
    elif not name and location != 'shared':
        # params = (
        return (
            ('location', 'device-group'),
            ('device-group', location),
            ('input-format', 'json'),
            ('output-format', 'json')
        )
    else:
        raise ParamsError(
            f"Unable to define combination name={name}, location={location}")

def create_url_base(device: str, version: str) -> str:
    """
    Creates a baseline URL for RestAPI calls
    params device: FQDN or IP address of device.
    type device: str
    params version: Version value of device must be str in '<num>.<num>' format
        or 'xml' to return XML type call.
    type version: str
    """
    try:
        if version == 'xml':
            url = BASEURL[version].format(device, version)
        elif float(version) > 10:
            url = BASEURL['latest'].format(device, version)
        else:
            url = BASEURL[version].format(device, version)
        return url
    except KeyError as err:
        raise PaloAltoAPIError(f"Cannot retreive correct Base URL from version={version} error={err}")

class Url:
    """
    URL Class
    """
    #value_list = ["url", "params", "headers"]
    @staticmethod
    def get_version(device, key):
        """
        Gets Device Version
        """
        return {
            "request_type": "GET",
            "url": f"https://{device}/api",
            "params": {
                "type": "op",
                "key": key,
                "cmd": "<show><system><info></info></system></show>"
            }
        }

    @staticmethod
    def key_gen(device, username, passwd):
        """
        Generates API Key
        """
        return {
            "request_type": "POST",
            "url": f"https://{device}/api",
            # "params": {
            #    "type": "keygen",
            #    "user": username,
            #    "password": passwd
            # },
            "params": None,
            "data": "password={}&user={}&type=keygen".format(passwd, username),
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }

    @staticmethod
    def xml_ha_get_status(device, key):
        """
        Gets HA Status
        """
        return {
            "request_type": "GET",
            "url": "https://{}/api".format(device),
            "params": {
                "type": "op",
                "key": key,
                "cmd": "<show><high-availability><state/></high-availability></show>"
            }
        }
    # Device group Gets all device groups and it's members

    @staticmethod
    def xml_device_entries(device, key):
        """
        Get Device Gropus
        """
        return {
            "request_type": "GET",
            "url": "https://{}/api/".format(device),
            "params": {
                "xpath": "/config/readonly/devices/entry[@name='localhost.localdomain']/device-group",
                "key": key,
                "type": "config",
                "action": "get"
            }
        }

    # Policies
    @staticmethod
    def restapi_policy_getpostrule(device, key, version='9.0', device_group="shared", name=None):
        """
        Uses Rest API to get Security Post Rules
        """
        return {
            "request_type": "GET",
            #"url": "https://{}/restapi/{}/Policies/SecurityPostRules".format(device, version),
            "url": "{}/Policies/SecurityPostRules".format(create_url_base(device, version)),
            "params": define_params(location=device_group, name=name),
            "headers": {
                "X-PAN-KEY": key
            }
        }

    @staticmethod
    def restapi_policy_getprerule(device, key, version='9.0', device_group="shared", name=None):
        """
        Uses Rest API to get Security Pre Rule
        """
        return {
            "request_type": "GET",
            #"url": "https://{}/restapi/{}/Policies/SecurityPreRules".format(device, version),
            "url": "{}/Policies/SecurityPreRules".format(create_url_base(device, version)),
            "params": define_params(location=device_group, name=name),
            "headers": {
                "X-PAN-KEY": key
            }
        }

    # Objects
    ## Applications
    @staticmethod
    def restapi_object_appgroups(device, key, version='9.0', device_group="shared", name=None):
        """
        Rest API Obect App Group
        """
        return {
            "request_type": "GET",
            #"url": "https://{}/restapi/{}/Objects/ApplicationGroups".format(device, version),
            "url": "{}/Objects/ApplicationGroups".format(create_url_base(device, version)),
            "params": define_params(location=device_group, name=name),
            "headers": {
                "X-PAN-KEY": key
            }
        }
    @staticmethod
    def restapi_object_app(device, key, version='9.0', device_group="shared", name=None):
        """
        Rest API Object APPs
        """
        return {
            "request_type": "GET",
            #"url": "https://{}/restapi/{}/Objects/Applications".format(device, version),
            "url": "{}/Objects/Applications".format(create_url_base(device, version)),
            "params": define_params(location=device_group, name=name),
            "headers": {
                "X-PAN-KEY": key
            }
        }
    ## URL Categories
    @staticmethod
    def restapi_object_url(device, key, version='9.0', device_group='shared', name=None):
        return {
            "request_type": "GET",
            #"url": "https://{}/restapi/{}/Objects/CustomURLCategories".format(device, version),
            "url": "{}/Objects/CustomURLCategories".format(create_url_base(device,version)),
            "params": define_params(location=device_group, name=name),
            "headers": {
                "X-PAN-KEY": key
            }
        }
    @staticmethod
    def restapi_object_url_categories(device, key, version='9.0',
                                device_group='shared', name=None,
                                member: List[str] = None, description: str = "URL Object",
                                url_type: str = "URL List",
                                request_type: str = 'list') -> List[dict]:
        """
        Rest API Url Category
        """
        if request_type == 'list':
            data = None
        else:
            data = json.dumps({
                "entry": [
                    {
                        "@name": name,
                        "description": description,
                        "list": {
                            "member": member
                        },
                        "type": url_type
                    }
                ]
            })
        request_options = {
            "create": "POST",
            "edit": "PUT",
            "list": "GET"
        }
        values = {
            #"request_type": "GET",
            "request_type": request_options[request_type],
            #"url": "https://{}/restapi/{}/Objects/CustomURLCategories".format(device, version),
            "url": "{}/Objects/CustomURLCategories".format(create_url_base(device,version)),
            "params": define_params(location=device_group, name=name),
            "headers": {
                "X-PAN-KEY": key
            },
            "input-format": "json",
            "output-format": "json",
        }

        req = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                    params=values.get('params', None), headers=values.get('headers', None),
                    data=data)
        #return req
        try:
            if req.json().get('@status'):
                if req.json().get('result'):
                    return req.json()['result']['entry']
                else:
                    return 'success'
            else:
                return None
        except KeyError:
            return None

        #try:
        #    return req.json()['result']['entry']
        #except KeyError:
        #    return None

    # WARNING The below are action items
    @staticmethod
    def xml_ha_suspend(device, key):
        """Caution with using this.. It will suspend a device. Requires Post Action"""
        return {
            "request_type": "GET",
            "url": "https://{}/api".format(device),
            "params": {
                "type": "op",
                "key": key,
                "cmd": "<request><high-availability><state><suspend/></state></high-availability></request>"
            }
        }

    @staticmethod
    def xml_ha_functional(device, key):
        """Caution with using this..."""
        return {
            "request_type": "GET",
            "url": "https://{}/api".format(device),
            "params": {
                "type": "op",
                "key": key,
                "cmd": "<request><high-availability><state><functional/></state></high-availability></request>"
            },
            #"headers": {
            #    "X-PAN-KEY": key
            #}
        }

    # Dynamic Address Group (TAGS)
    @staticmethod
    def xml_get_dynamic_address_group(device: str, api_key: str, name: str = 'all', cert = False):
        """
        XML Get DAG
        """
        if name == 'all':
            values = {
                "request_type": "POST",
                "url": "https://{}/api".format(device),
                "params": {
                    "type": "op",
                    "cmd" : "<show><object><dynamic-address-group><all></all></dynamic-address-group></object></show>",
                },
                "headers": {
                    "X-PAN-KEY": api_key
                }
            }
        req = ApiCalls.request(url=values['url'], req_type=values['request_type'],
            params=values['params'],
            headers=values['headers'], verify=cert)
        return req
    @staticmethod
    def xml_get_registered_ip(device: str, api_key: str, tag: str, cert = False):
        """
        Used to Get XML registered IP
        """
        values = {
            "request_type": "POST",
            "url": "https://{}/api".format(device),
            "params": {
                "type": "op",
                "cmd" : "<show><object><registered-ip><tag><entry name='{}'/></tag></registered-ip></object></show>".format(tag),
            },
            "headers": {
                "X-PAN-KEY": api_key
            },
        }
        req = ApiCalls.request(url=values['url'], req_type=values['request_type'], params=values['params'],
                        headers=values['headers'], data=None, verify=cert)
        #return reformat_xml(ApiCalls.request(url=values['url'], req_type=values['request_type'],
        #                                params=values['params'],
        #                                headers=values['headers'], data=None, verify=cert))
        #return extract_registered_ip(r)
        return req

    # TO DO: Need to build a self test that checks for a long list and cuts it down into chungs.
    # this should prevent issues with a too long request over 2048 i think is the limit
    @staticmethod
    def xml_delete_registered_ip(device: str, api_key: str,
                            tag: str, ip_list: List[str], cert = False):
        """
        XML Delete Register IP for DAGS
        """
        item_list = []
        for addr in ip_list:
            item_list.append(xml_unregister_tag['item'].format(addr, tag))
        values = {
            "request_type": "POST",
            "url": "https://{}/api".format(device),
            "params": {
                "type": "user-id",
                "cmd": xml_unregister_tag['form'].format(('').join(item_list))
            },
            "headers": {
                "X-PAN-KEY": api_key,
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
        req = ApiCalls.request(url=values['url'], req_type=values['request_type'],
                        params=values['params'],
                        headers=values['headers'], verify=cert)
        return req

    @staticmethod
    def xml_add_registered_ip(device: str, api_key: str, tag: str,
                        ip_list: List[str], persistent: int,
                        timeout: int,  cert = False) -> Response:
        """
        param persistant: The default is 1, which means that the tagging will
            survive reboots of the Firewall. Options 0 or 1.
        type persistant: int
        param timeout: optional timeout parameter, to specify the expiration
            in seconds of the tag. The default is 0, which means 'never expire'.
            The maximum value is 2592000 (30 days).
        type timeout: int
        """
        item_list = []
        for addr in ip_list:
            item_list.append(xml_register_tag['item'].format(addr, persistent, timeout, tag))
        values = {
            "request_type": "POST",
            "url": "https://{}/api".format(device),
            "params": {
                "type": "user-id",
                "cmd": xml_register_tag['form'].format(('').join(item_list))
            },
            "headers": {
                "X-PAN-KEY": api_key,
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
        req = ApiCalls.request(url=values['url'], req_type=values['request_type'],
                        params=values['params'],
                        headers=values['headers'], data=None, verify=cert)
        return req

class ApiCalls:
    """Used for Static Method API Calls"""
    @staticmethod
    def request_post(url, params=None, data=None, headers=None, verify=False):
        """
        POST Request
        """
        try:
            req = requests.post(url, params=params, data=data,
                              headers=headers, verify=verify)
            req.raise_for_status()
            return req
        except (SSLError, HTTPError, Exception, TypeError) as err:
            raise PaloAltoAPIError(err)

    @staticmethod
    def request_get(url, params=None, headers=None, verify=False):
        """
        GET Request
        """
        try:
            req = requests.get(url, params=params,
                             headers=headers, verify=verify)
            req.raise_for_status()
            return req
        except (SSLError, HTTPError, Exception, TypeError) as err:
            raise PaloAltoAPIError(err)

    # New function to take over
    @staticmethod
    def request(url, req_type: str="GET", params: dict=None,
            headers: dict=None, data: Dict[str, Any]=None, verify = None):
        """
        REQUEST
        """
        verify = config.CERT if verify is None else verify
        # Convert to JSON object to pass as payload
        if not isinstance(data, str):
            data = json.dumps(data) if data is not None else None
        try:
            req = requests.request(
                method=req_type, url=url, params=params, headers=headers, data=data, verify=verify)
            if req.status_code == 400:
                # Bad request provides a error message
                return req
            req.raise_for_status()
            #req.json()['error'] = False
            return req #xmltodict.parse(r.text)["response"]["result"]["system"]
        except (Exception, ConnectionError) as err:
            raise PaloAltoAPIError(str(err).replace(headers['X-PAN-KEY'], '****'))
