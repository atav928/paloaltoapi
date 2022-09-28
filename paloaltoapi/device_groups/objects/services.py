"""Services"""

from paloaltoapi.exceptions import PaloAltoAPIError, PaloAltoMissingParam
from paloaltoapi.urls import get_restapi


class Services:
    def __init__(self, location: str, api_key: str, device: str, version: str, name: str = None,
                 certstore=None, output_format: str = "json"):
        self.api_key = api_key
        self.version = version
        self.device = device
        self.location = location
        self.name = name
        self.certstore = certstore
        self.output_format = output_format


class FirewallServices(Services):
    """Firewall based Services call

    Args:
        Services (_type_): _description_
    """
    FIREWALL_SERVICES = ['predefined', 'shared', 'vsys', 'panorama-pushed']
    # TODO: build out Firewall service calls

    def __init__(self, location: str, api_key: str, device: str, version: str, name: str = None,
                 certstore=None, output_format: str = "json", vsys: str = 'vsys1'):
        self.vsys = vsys
        super().__init__(location=location, api_key=api_key, device=device,
                     version=version, name=name, certstore=certstore, output_format=output_format)
        self.services = {}

    def refresh_services(self):
        """_summary_

        Raises:
            PaloAltoMissingParam: _description_
        """
        # TODO: build out
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
                           certstore, url_type='services', version=self.version)
        self.services[self.location] = resp.json()["result"]



class PanoramaServices(Services):
    """Panorama based Services

    Args:
        location (str): Location to search values ['all', 'shared', 'predefined', 'device-group']
        api_key (str): Token for Panorama Device
        device (str): Panorama FQDN or IP
        version (str): PAN-OS version needed to form RestAPI call.
        name (str): Optional name of service if known. Default=None,
        certstore (str|bool): Optional Specify True or False to use
                            certificate verification. If using custom 
                            certificate enter location for trusted cert. 
                            Default=None
        output_format (str): Optional Default="json"
        device_group (str): Required if location is 'device-group'. Default=None
        device_group_list (list): Required if location is set to 'all'. Default=None

    Returns:
        services (dict): returns the list of services in location specified
    """

    def __init__(
            self, location: str, api_key: str, device: str, version: str, name: str = None,
            certstore=None, output_format: str = "json", device_group: str = None,
            device_group_list: list = None):
        super().__init__(location=location, api_key=api_key, device=device,
                         version=version, name=name, certstore=certstore, output_format=output_format)
        self.device_group = device_group
        self.device_group_list = device_group_list
        self.services: dict = {}
        self.refresh_services()

    def refresh_services(self):
        """Refreshes the services dictionary
        """
        if self.location.lower() == 'all':
            self.services_in_all()
        elif self.location.lower() in ['predefined', 'shared']:
            self.services_in_predefined_or_shared()
        elif self.location.lower() == 'device-group':
            self.services_in_device_groups()

    def services_in_all(self):
        """Retrieves all services requires device group list to be defined
        """
        for loc in ['predefined', 'shared', 'device-group']:
            print(f"getting {loc}")
            if loc == 'device-group':
                self.services_in_device_groups_all()
            else:
                resp = get_restapi(device=self.device, api_key=self.api_key,
                                   device_group=loc, name=self.name, verify=self.
                                   certstore, url_type='services', version=self.version)
                self.services[loc] = resp.json()["result"]

    def services_in_device_groups(self):
        """retrieves just the device groups either name defined or if a
         specific device group requested
        """
        if not self.services.get('device-group'):
            self.services['device-group'] = {}
        if self.name and self.device_group:
            resp = get_restapi(
                device=self.device, api_key=self.api_key, name=self.name,
                verify=self.certstore, url_type='services', version=self.version,
                device_group=self.device_group)
            self.services['device-group'][self.device_group] = resp.json()["result"]
        else:
            resp = get_restapi(
                device=self.device, api_key=self.api_key,
                verify=self.certstore, url_type='services', version=self.version,
                device_group=self.device_group)
            self.services['device-group'][self.device_group] = resp.json()["result"]

    def services_in_device_groups_all(self):
        """Goes through entire list of device groups and pulls each services defined

        Raises:
            PaloAltoMissingParam: _description_
        """
        if not self.services.get('device-group'):
            self.services['device-group'] = {}
        print(f"Device Group: {self.device_group_list}")
        if self.device_group_list:
            for dev_grp in self.device_group_list:
                print(f'getting {dev_grp}')
                resp = get_restapi(
                    device=self.device, api_key=self.api_key,
                    verify=self.certstore, url_type='services', version=self.version,
                    device_group=dev_grp)
                self.services['device-group'][dev_grp] = resp.json()["result"]
        else:
            raise PaloAltoMissingParam(
                "missing device-group parameter to get devicegroup services")

    def services_in_predefined_or_shared(self):
        """Used to generate a services list used for predefined or shared location types
        """
        resp = get_restapi(device=self.device, api_key=self.api_key,
                           device_group=self.location, name=self.name, verify=self.
                           certstore, url_type='services', version=self.version)
        self.services[self.location] = resp.json()["result"]
