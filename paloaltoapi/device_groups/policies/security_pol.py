"""Extract Security Polcies (Rules)"""

from typing import Any, Dict
from paloaltoapi import config
from paloaltoapi.exceptions import PaloAltoAPIError
from paloaltoapi.utils import get_version

from . import add_obj_to_rule, check_chg_number, delete_obj_from_rule

class SecurityPolicies:
    """
    Security Rule Policy Module
    """
    def __init__(self, device: str, key: str, version: str = None,
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
            version = get_version(
                device=device,api_key=key)
        self.version = version
        self.device = device
        self.security_policies = {}
        self.api_key = key
        self.certstore = certstore if certstore is not None else config.CERT

    def modify_security_rule(self, action: str, rule: Dict[str, Any], chg_number: str):
        """Modifies the Security rule; based on cusomized Decom Resluts
        :params action: delete or add
        :params decom_task: dictionary response from decom rule task
        :params chg_number: Chnage or INC number
        """
        # raise error if change number not compliant
        if not check_chg_number(chg_number):
            raise PaloAltoAPIError(chg_number)
        if action == 'delete':
            resp = delete_obj_from_rule(rule=rule,device=self.device,chg_number=chg_number,
                                        api_key=self.api_key,verify=self.certstore)
        elif action in ['add','set']:
            resp = add_obj_to_rule(rule=rule,device=self.device,chg_number=chg_number,
                                    api_key=self.api_key,verify=self.certstore)
        else:
            raise PaloAltoAPIError
        return resp
