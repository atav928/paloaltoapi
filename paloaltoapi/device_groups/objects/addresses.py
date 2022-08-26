"""Panorama Address Objects"""

from typing import Any, Dict
from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoAPIError, PaloAltoObjExists,\
    PaloAltoObjNotExists, PaloAltoTAGError
from paloaltoapi.utils import get_version
from . import _address_xml_search, _extract_address,\
    create_address, create_address_data, delete_address
from .tags_obj import check_if_tag_exists

class AddressesObj:
    """
    Getting and Manipulating Address Objects in Panorama
    """
    def __init__(self, device: str, api_key: str, version: str = None,
                 certstore=None):
        """
        Set up palo alto NAT Policy OBject from Panorama\n
        Keyword Arguments:
        ------------
            \tdevice {str} -- FQDN of Panorama Object\n
            \tkey {str} -- Palo Alto API Key\n
            \tversion {str} -- Palo Alto major release version ex: 9.x 10.x (default: {None})\n
            \tcertstore {str|bool} -- Verification on/off or supply
             custom cert store fore SSL (default: {None})
        """
        if not version:
            version = get_version(device=device, api_key=api_key)
        self.version = version
        self.device = device
        self.addresses = {}
        self.api_key = api_key
        self.certstore = certstore if certstore else config.CERT

    def get_address_obj_by_name(self, address_names: list) -> dict:
        """
        Using the Address Name of an Object find and resolve the address.
        Does not look at location of device. That would need to be built out.
        Or use RestAPI to pull the object if the information is known.
        Keyword Arguments:
        -----------------
        address_names {List[str]} -- Address Object Name in list format to
        Return:
        ------
        result {dict} -- {address_name: value(IP or FQDN)}
        """
        result = {}
        search = config.GLOBAL_SEARCHES['addresses_xml']
        for address in address_names:
            entry = _address_xml_search(search_params=search, obj=address,
                                        device=self.device, api_key=self.api_key,
                                        certstore=self.certstore)
            addr_value = _extract_address(entry=entry)
            result.update({address: addr_value})
        return result

    def add_address_obj(self, address_name: str,
                        location: str = 'shared', fqdn: str = None,
                        ip_netmask: str = None, **kwargs):
        """Add Address Object to Palo Alto"""
        results = {}
        test = self.get_address_obj_by_name([address_name])
        # Ensure proper fields are filled out
        if test[address_name]:
            raise PaloAltoObjExists(f'address_obj={address_name} alread exists')
        if not ip_netmask and not fqdn:
            raise PaloAltoAPIError('Requires an ip-netmask or fqdn')
        # Build Payload
        kwargs['address_name'] = address_name
        kwargs['ip_netmask'] = ip_netmask
        kwargs['location'] = location
        kwargs['fqdn'] = fqdn
        data = create_address_data(kwargs)
        if (data['entry'][0].get('tag') and
            not check_if_tag_exists(data['entry'][0]['tag']['member'], device=self.device,
                                       certstore=self.certstore,api_key=self.api_key)):
            raise PaloAltoTAGError
        results = create_address(address_name,location,version=self.version,
                                device=self.device,api_key=self.api_key,
                                certstore=self.certstore,data=data)
        del data
        return results

    def delete_address_obj(self, address_name: str,
                        location: str = 'shared') -> Dict[str, Any]:
        """Delete Address Object to Palo Alto; requires that object exist. Addes an 'error'
        field to the json response to determine if there was a problem handling the request.
        :param address_name: Required, Address Object Name
        :type address_name: str
        :param location: Optional, defaults to 'shared' or can be a device-group name
        :type location: str
        :rtype: Dict
        """
        results = {}
        test = self.get_address_obj_by_name([address_name])
        # Checks if Address Obj Exists returns error if doesnot
        if not test[address_name]:
            raise PaloAltoObjNotExists(address_name)
        results = delete_address(name=address_name,location=location,version=self.version,
                                device=self.device,api_key=self.api_key,
                                verify=self.certstore)
        return results
