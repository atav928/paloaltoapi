"""Address Groups"""

from typing import Any, Dict, List
from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoAPIError, PaloAltoObjExists,\
    PaloAltoTAGError, PaloAltoTaskError
from paloaltoapi.utils import get_version
from .tags_obj import check_if_tag_exists
from . import _address_grp_xml_search, create_address_grp
from . import create_address_grp_data, list_address_grp, update_address_grp
from .utils import add_obj_to_address_group, delete_obj_from_address_group

class AddressGroups:
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
        self.certstore = certstore if certstore is not None else config.CERT

    def get_address_group_by_name(self, address_groups: List[str]) -> Dict[str,Any]:
        """
        Using the Address Name of an Object find and resolve the address.
        Does not look at location of device. That would need to be built out.
        Or use RestAPI to pull the object if the information is known.
        Keyword Arguments:
        -----------------
        address_groups {List[str]} -- Address Group Names in list format to
        Return:
        ------
        result {dict} -- {address_name: value(IP or FQDN)}
        """
        result = {}
        search = config.GLOBAL_SEARCHES['address_groups_xml']
        for addr_grp in address_groups:
            addr_grp_value = _address_grp_xml_search(search_params=search, obj=addr_grp,
                                        device=self.device, api_key=self.api_key,
                                        certstore=self.certstore)
            result.update({addr_grp: addr_grp_value})
        return result

    def list_address_group(self, address_grp: str,
                        location: str = 'shared') -> list:
        """Get a list of current Address Groups"""
        test = self.get_address_group_by_name([address_grp])
        # Ensure proper fields are filled out
        if not test[address_grp]:
            raise PaloAltoObjExists(f'address_group={address_grp} does not exists')
        results = list_address_grp(address_grp, location=location, version=self.version,
                                   api_key=self.api_key,certstore=self.certstore,
                                   device=self.device)
        return results['result']['entry'][0]['static']['member']

    def add_address_group(self, address_grp: str, address_members: list,
                        location: str = 'shared', **kwargs):
        """Addes a Address Group Obj"""
        results = {}
        test = self.get_address_group_by_name([address_grp])
        # Ensure proper fields are filled out
        if test[address_grp]:
            raise PaloAltoObjExists(f'address_group={address_grp} alread exists')
        if not isinstance(address_members, list):
            raise PaloAltoAPIError('Requires an Address Member List')

        # Build Payload
        kwargs['address_grp'] = address_grp
        kwargs['address_members'] = address_members
        kwargs['location'] = location
        data = create_address_grp_data(kwargs)
        # Test if tag was passed and is valid
        if (data['entry'][0].get('tag') and
            not check_if_tag_exists(data['entry'][0]['tag']['member'], device=self.device,
                                       certstore=self.certstore,api_key=self.api_key)):
            raise PaloAltoTAGError
        #TODO: Testing out how this would work
        results = create_address_grp(address_grp,location,version=self.version,
                                device=self.device,api_key=self.api_key,
                                certstore=self.certstore,data=data)
        return results

    def update_address_group(self, address_grp: str, address_members: list,
                        location: str = 'shared', **kwargs):
        """Addes a Address Group Obj"""
        results = {}
        test = self.get_address_group_by_name([address_grp])
        # Ensure proper fields are filled out
        if not test[address_grp]:
            raise PaloAltoObjExists(f'address_group={address_grp} does not exists')
        if not isinstance(address_members, list):
            raise PaloAltoAPIError('Requires an Address Member List')
        # If it returns with a 400 ERROR that usually means a static item doesn't exist
        # may need to build out an ADDRESS check or find a better way to handle
        # Build Payload
        kwargs['address_grp'] = address_grp
        kwargs['address_members'] = address_members
        kwargs['location'] = location
        data = create_address_grp_data(kwargs)
        # print(data)
        # Test if tag was passed and is valid
        if (data['entry'][0].get('tag') and
            not check_if_tag_exists(data['entry'][0]['tag']['member'], device=self.device,
                                       certstore=self.certstore,api_key=self.api_key)):
            raise PaloAltoTAGError
        results = update_address_grp(address_grp,location,version=self.version,
                                device=self.device,api_key=self.api_key,
                                certstore=self.certstore,data=data)
        del data
        return results

    def modify_address_group(self, action: str, members: list, address_group: str,
                            location: str='shared') -> Dict[str,list]:
        """Part of SVC DECOM TASKS function. Used to modify an existing Address Group
         Object by either removing or adding an address member.
          Address member must already exist.
          :params action: Valid values ['add','remove','delete']
          :type action: str
          :params members: list of addresses to remove from address group
          :type members: List[str]
          :params address_group: Address Group Name to edit
          :type address_group: str
          :params location: either 'shared' or device-group name
          :type location: str
          """
        action = action.lower()
        if action not in ['add','remove','delete']:
            raise PaloAltoTaskError(action)
        results = {}
        result_list = []
        if action == 'add':
            for member in members:
                resp = add_obj_to_address_group(device=self.device,token=self.api_key,
                                                verify=self.certstore,location=location,
                                                member=member, address_group=address_group)
                result_list.append(resp['response'])
        if action in ['remove', 'delete']:
            for member in members:
                resp = delete_obj_from_address_group(device=self.device,token=self.api_key,
                                                    verify=self.certstore,location=location,
                                                    member=member, address_group=address_group)
                result_list.append(resp['response'])
        results['response'] = result_list
        return results
