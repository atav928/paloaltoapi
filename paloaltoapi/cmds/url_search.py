"""Searches for a URL Category"""

from typing import Any, Dict

from paloaltoapi.firewall import Firewall
from paloaltoapi.cmds import xml_cmd_call
from paloaltoapi.utils import define_certstore, get_version

class UrlSearch(Firewall):
    """Searches for a url search must be a firewall not supported in Panorama"""
    def __init__(self, device: str, api_key: str, version: str = None,
                 certstore=None):
        """
        Requires a Firewall endpoint api key can use Firewall module to generate
         and pass. This will just query the local URL DB and return it's results\n
        Keyword Arguments:
        ------------
            \tdevice {str} -- FQDN of Panorama Object\n
            \tkey {str} -- Palo Alto API Key\n
            \tversion {str} -- Palo Alto major release version ex: 9.x 10.x (default: {None})\n
            \tcertstore {str|bool} -- Verification on/off or supply
             custom cert store fore SSL (default: {None})
        """
        super().__init__(device=device, username=None, passwd=None, certstore=certstore,key=api_key)
        if not version:
            version = get_version(device=device, api_key=api_key,certstore=certstore)
        self.version = version
        self.device = device
        self.addresses = {}
        self.api_key = api_key
        self.certstore = define_certstore(certstore)

    def search_url(self, domain: str) -> Dict[str, Any]:
        """Search for a URL"""
        command = f'<test><url>{domain}</url></test>'
        resp = xml_cmd_call(device=self.device,cmd=command,api_key=self.api_key,
                    certstore=self.certstore)
        return resp
