"""
https://panorama.example.com/restapi/9.0/Objects/CustomURLCategories
Sample Params
params = {"location":"shared","output-format":"json","input-format":"json"}
"""
from typing import List
from paloaltoapi.urls import ApiCalls, Url
from paloaltoapi.exceptions import PaloAltoAPIError, UrlExistsError, UrlNotExistsError
from paloaltoapi.utils import get_version

class UrlCategories:
    """
    Creates a Url Category
    """
    def __init__(self, device: str, api_key: str, version: str = None, certstore=None):
        self.device = device
        self.url_categories = { }
        self.api_key = api_key
        self.certstore = certstore
        if not version:
            version = get_version(device=device, api_key=api_key,certstore=certstore)
        self.version = version

    def __str__(self):
        return self.device

    def _get_url_cust_categories(self, device_group='shared') -> list:
        """
        Function used for Panorama
        params name: Url Name
        type name: str
        params device_group: Device group to get
         type device_group: str
        """
        # TODO: This willl only work for Panorama, need to refactor
        # to work for Firewall as well
        values = Url.restapi_object_url(self.device, self.api_key,
                                        version=self.version,
                                        device_group=device_group)
        req = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                            params=values.get('params', None),
                            headers=values.get('headers', None),
                            data=values.get('data', None),
                            verify=self.certstore)
        jsondata = req.json()
        if jsondata['@status'] != 'success':
            raise PaloAltoAPIError(
                "Unable to retrieve rules for {} response: {}".format(device_group, jsondata))
        else:
            # Only works with valid name objects
            try:
                setattr(self, device_group, {'objects': {'url-categories':
                    {'entry': jsondata['result']['entry']}}})
                # Update internal URL Categories
                self.url_categories.update({device_group: jsondata['result']['entry']})
                return jsondata['result']['entry']
            except KeyError:
                setattr(self, device_group, {'objects': {'url-categories':
                    {'entry': []}}})
                self.url_categories.update({device_group: []})
                return []

    def _get_url_cust_categories_by_name(self, name, device_group='shared') -> str:
        """
        Function used for Panorama to retrieve a category name from a specific device-group
        params name: Url Name
        type name: str
        params device_group: Device group to get
         type device_group: str
        """
        # TODO: This willl only work for Panorama, need to refactor
        # to work for Firewall as well
        values = Url.restapi_object_url(self.device, self.api_key,
                                        name=name, version=self.version,
                                        device_group=device_group)
        req = ApiCalls.request(req_type=values['request_type'], url=values['url'],
                            params=values.get('params', None),
                            headers=values.get('headers', None),
                            data=values.get('data', None),
                            verify=self.certstore)

        jsondata = req.json()
        if jsondata['@status'] != 'success':
            raise PaloAltoAPIError(
                "Unable to retrieve rules for {} response: {}".format(device_group, jsondata))
        else:
            # Returns just the entry name being requested
            return jsondata['result']['entry']

    # Direct Access Functions within the URL Category
    def list_url_category(self, name: str = None, device_group: str = None) -> dict:
        """
        Get a URL List based on the name provided. Returns None if not found.
        """
        if name and not device_group:
            raise PaloAltoAPIError(f'name={name} was supplied without a device group')
        if not name and not device_group:
            raise PaloAltoAPIError('Currently does not support no device group')

        if not name and device_group:
            return self._get_url_cust_categories(device_group=device_group)
        else:
            return Url.restapi_object_url_categories(name=name, device_group=device_group,
                            version=self.version, key=self.api_key,
                            device=self.device, request_type='list')

    def edit_url_category(self, name: str, member: List[str],
                            device_group: str, description: str = "URL Category",
                            url_type: str = "URL List"):
        """
        Edits existing URL
        """
        #if location.lower() not in VALID_LOCATION:
        #   raise PaloAltoAPIError(f"Invalid Location type: {location}")
        #if not self.list_url_category(name=name, device_group=device_group):
        #    raise PaloAltoAPIError(f"Unable to fund url-category={name}")
        self.__edit_check_url_exists(name=name, device_group=device_group)
        # Verify that the name exists by getting it first.
        # Raise error to try to Create Object

        if not isinstance(member, list):
            member=[member]
        # If error is not raised than go ahead and edit the existing URL Category
        return Url.restapi_object_url_categories(name=name, device_group=device_group,
                        version=self.version, key=self.api_key,
                        device=self.device, description=description,
                        url_type=url_type, member=member,
                        request_type='edit')

    def create_url_category(self, name: str, member: List[str],
                        device_group: str, description: str = "URL Category",
                        url_type: str = "URL List"):
        """
        Create URL Category
        """

        self.__create_check_url_exists(name=name, device_group=device_group)
        #if self.list_url_category(name=name, device_group=device_group):
        #    raise PaloAltoAPIError(
        #        f"URL Category name={name} exists already in device-group={device_group}")

        if not isinstance(member, list):
            member=[member]

        return Url.restapi_object_url_categories(name=name, device_group=device_group,
                        version=self.version, key=self.api_key,
                        device=self.device, description=description,
                        url_type=url_type, member=member, request_type='create')

    def __create_check_url_exists(self, name: str, device_group:str):
        """
        Running a quick check to see if the URL exists or not for a creation rule.
        If it exists it will return UrlExistsError, this will pass on anyother error,
        but that should be caught by default PaloAltoAPIError in the call
        """
        try:
            if self.list_url_category(name=name, device_group=device_group):
                raise UrlExistsError(
                        f"URL Category name={name} exists already in device-group={device_group}")
        except PaloAltoAPIError:
            pass

    def __edit_check_url_exists(self, name: str, device_group:str):
        """
        Running a check against an Edit. If the URL Exists we are good
        if it does not raise URL Does Not Exist error.
        """
        try:
            if self.list_url_category(name=name, device_group=device_group):
                pass
        except PaloAltoAPIError:
            raise UrlNotExistsError(
                        f"URL Category name={name} does not exist in device-group={device_group}")
