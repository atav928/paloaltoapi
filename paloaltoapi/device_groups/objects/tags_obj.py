"""Call on Palo Alto Tag Object"""

from paloaltoapi import config
from paloaltoapi.device_groups.objects import _tags_xml_search
from paloaltoapi.exceptions import PaloAltoTAGError, ParamsError
from paloaltoapi.utils import get_version

def check_if_tag_exists(check_tags: list, **kwargs) -> bool:
    """Checks if tag exists in Shared area to be able to add an object if a tag is required"""
    device = kwargs.get('device')
    certstore = kwargs.get('certstore')
    api_key = kwargs.get('api_key')
    #print(f'checking tags {check_tags}')
    ## Checking Tags, but only supports Shared Tags
    verify_tags = _verify_tags(tags=check_tags,api_key=api_key,
                                device=device,certstore=certstore)
    for key, value in verify_tags.items():
        #print(f'key={key} value={value}')
        if value is None or value.get('location-type') != 'shared':
            #print('fail')
            raise PaloAltoTAGError(f'tag={key}')
    return True

def _verify_tags(**kwargs):
    """Verify if tags exist"""
    result = {}
    device = kwargs.get('device')
    certstore = kwargs.get('certstore')
    api_key = kwargs.get('api_key')
    tags = kwargs['tags']
    print(tags)
    if not device or not api_key:
        raise ParamsError('device=None, api_key=None')
    tag_obj = Tags(device=device,api_key=api_key,certstore=certstore)
    for tag in tags:
        result[tag] = tag_obj.get_tags(tag)
    return result

class Tags:
    """
    Getting and Manipulating Address Objects in Panorama
    """
    def __init__(self, device: str, api_key: str, version: str = None,
                 certstore=None):
        """
        Set up palo alto Tag Object from Panorama\n
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
        self.tag = {}
        self.api_key = api_key
        self.certstore = certstore if certstore else config.CERT

    def get_tags(self, tags: str):
        """Retrieve a tag from PA based off name"""
        search = config.GLOBAL_SEARCHES['tags_xml']
        entry = _tags_xml_search(search_params=search, obj=tags,
                                 device=self.device, api_key=self.api_key,
                                 certstore=self.certstore)
        return entry
