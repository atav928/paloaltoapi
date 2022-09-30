"""Services"""

from paloaltoapi.exceptions import PaloAltoAPIError, PaloAltoMissingParam
from paloaltoapi.urls import get_restapi


class Applications:
    """Applications Base class
    """

    def __init__(self, api_key: str, device: str, version: str,
                 certstore=None, output_format: str = "json"):
        self.api_key = api_key
        self.version = version
        self.device = device
        self.certstore = certstore
        self.output_format = output_format
        self.applications: dict = {}
        self.url_type: str = "applications"


class FirewallApplications(Applications):
    """Firewall based Services call

    Args:
        Services (_type_): _description_
    """
    FIREWALL_SERVICES = ['predefined', 'shared', 'vsys', 'panorama-pushed']
    # TODO: build out Firewall service calls

    def __init__(self, device: str, api_key: str, version: str,
                 certstore=None, output_format: str = "json"):
        super().__init__(device=device, api_key=api_key,
                         version=version, certstore=certstore, output_format=output_format)
        self.services = {}
        self.name = None
        self.location = None
        self.vsys = 'vsys'

    def get_services(self, location: str, name: str = None):
        """_summary_

        Raises:
            PaloAltoMissingParam: _description_
        """
        # TODO: build out
        self.location = location
        self.name = name
        if self.location not in self.FIREWALL_SERVICES:
            raise PaloAltoMissingParam(f'invalid location: {self.location}')

    def services_in_vsys(self):
        """_summary_
        """
        # TODO: Build out
        pass

    def services_in_firewall(self):
        """Used to generate a services list used for predefined or shared location types
        """
        resp = get_restapi(device=self.device, api_key=self.api_key,
                           device_group=self.location, name=self.name, verify=self.
                           certstore, url_type=self.url_type, version=self.version)
        self.services[self.location] = resp.json()["result"]


class PanoramaApplications(Applications):
    """Panorama based Services

    Args:
        api_key (str): Token for Panorama Device
        device (str): Panorama FQDN or IP
        version (str): PAN-OS version needed to form RestAPI call.
        certstore (str|bool, optional): Optional Specify True or False to use
                            certificate verification. If using custom
                            certificate enter location for trusted cert.
                            Default=None
        output_format (str, optional): Default="json"

    Returns:
        services (dict): returns the list of services in location specified
    """
    PANORAMA_APPLICATIONS = ['predefined', 'shared', 'device-group']

    def __init__(self, **kwargs):
        super().__init__(
            api_key=kwargs['api_key'],
            device=kwargs['device'],
            version=kwargs['version'],
            certstore=kwargs.get('certstore', None),
            output_format=kwargs.get('output_format', 'json'))
        self.device_group: str = None
        self.device_group_list: list = None
        self.name: str = None
        self.location = None

    def get_applications(self, location: str, name: str = None, device_group: str = None,
                         device_group_list=None) -> dict:
        """Retrieve Panorama Applications

        Args:
            location (str): Location to search values ['all', 'shared', 'predefined', 'device-group']
            name (str, optional): name of service if known. Default to None.
            device_group (str, optional|required): Required if location is 'device-group'. Defaults to None.
            device_group_list (list, optional|required): Required if location is set to 'all'. Defaults to None.

        Returns:
            _type_: _description_
        """
        self.location = location
        self.name = name
        self.device_group = device_group
        self.device_group_list = device_group_list
        if self.location.lower() == 'all':
            self._applications_in_all()
        elif self.location.lower() in ['predefined', 'shared']:
            self._applications_in_predefined_or_shared()
        elif self.location.lower() == 'device-group':
            self._applications_in_device_groups()
        else:
            raise PaloAltoMissingParam(f"unknown location: {self.location}")
        return self.applications

    def _applications_in_all(self):
        """Retrieves all services requires device group list to be defined
        """
        for loc in ['predefined', 'shared', 'device-group']:
            print(f"getting {loc}")
            if loc == 'device-group':
                self._applications_in_device_groups_all()
            else:
                resp = get_restapi(device=self.device, api_key=self.api_key,
                                   device_group=loc, name=self.name, verify=self.
                                   certstore, url_type=self.url_type, version=self.version)
                self.applications[loc] = resp.json()["result"]

    def _applications_in_device_groups(self):
        """retrieves just the device groups either name defined or if a
         specific device group requested
        """
        if not self.applications.get('device-group'):
            self.applications['device-group'] = {}
        if self.name and self.device_group:
            resp = get_restapi(
                device=self.device, api_key=self.api_key, name=self.name,
                verify=self.certstore, url_type=self.url_type, version=self.version,
                device_group=self.device_group)
            self.applications['device-group'][self.device_group] = resp.json()[
                "result"]
        else:
            resp = get_restapi(
                device=self.device, api_key=self.api_key,
                verify=self.certstore, url_type=self.url_type, version=self.version,
                device_group=self.device_group)
            self.applications['device-group'][self.device_group] = resp.json()[
                "result"]

    def _applications_in_device_groups_all(self):
        """Goes through entire list of device groups and pulls each services defined

        Raises:
            PaloAltoMissingParam: _description_
        """
        if not self.applications.get('device-group'):
            self.applications['device-group'] = {}
        print(f"Device Group: {self.device_group_list}")
        if self.device_group_list:
            for dev_grp in self.device_group_list:
                print(f'getting {dev_grp}')
                resp = get_restapi(
                    device=self.device, api_key=self.api_key,
                    verify=self.certstore, url_type=self.url_type, version=self.version,
                    device_group=dev_grp)
                self.applications['device-group'][dev_grp] = resp.json()["result"]
        else:
            raise PaloAltoMissingParam(
                "missing device-group parameter to get devicegroup services")

    def _applications_in_predefined_or_shared(self):
        """Used to generate a services list used for predefined or shared location types
        """
        resp = get_restapi(device=self.device, api_key=self.api_key,
                           device_group=self.location, name=self.name, verify=self.
                           certstore, url_type=self.url_type, version=self.version)
        self.applications[self.location] = resp.json()["result"]
