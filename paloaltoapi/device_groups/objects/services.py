"""Services"""

import threading

from paloaltoapi.exceptions import PaloAltoMissingParam
from paloaltoapi.urls import get_restapi


class Services:
    """Services Base Class
    """
    def __init__(self, api_key: str, device: str, version: str,
                 certstore=None, output_format: str = "json"):
        self.api_key: str = api_key
        self.version: str = version
        self.device: str = device
        self.certstore = certstore
        self.output_format: str = output_format
        self.services: dict = {}
        self.url_type: str = 'services'


class FirewallServices(Services):
    """Firewall based Services call

    Args:
        Services (_type_): _description_
    """
    FIREWALL_SERVICES = ['predefined', 'shared', 'vsys', 'panorama-pushed', 'all']
    # TODO: build out Firewall service calls

    def __init__(self, **kwargs):
        super().__init__(
            api_key=kwargs['api_key'],
            device=kwargs['device'],
            version=kwargs['version'],
            certstore=kwargs.get('certstore', None),
            output_format=kwargs.get('output_format', 'json'))
        self.name = None
        self.location = None
        self.vsys = 'vsys1'

    def get_services(self, location: str, name: str = None, vsys: str = 'vsys1'):
        """_summary_

        Raises:
            PaloAltoMissingParam: _description_
        """
        # TODO: build out
        self.location = location
        self.name = name
        self.vsys = vsys
        if self.location not in self.FIREWALL_SERVICES:
            raise PaloAltoMissingParam(f'invalid location: {self.location}')

    def _services_in_vsys(self):
        """_summary_
        """
        # TODO: Build out
        pass

    def _services_in_firewall(self):
        """Used to generate a services list used for predefined or shared location types
        """
        resp = get_restapi(device=self.device, api_key=self.api_key,
                           device_group=self.location, name=self.name, verify=self.
                           certstore, url_type=self.url_type, version=self.version)
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

    def __init__(self, **kwargs):
        super().__init__(
            api_key=kwargs['api_key'],
            device=kwargs['device'],
            version=kwargs['version'],
            certstore=kwargs.get('certstore', None),
            output_format=kwargs.get('output_format', 'json')
        )
        self.device_group: str = None
        self.device_group_list: list = None
        self.name: str = None
        self.location = None

    def get_services(self, location: str, name: str = None, device_group: str = None,
                     device_group_list: list = None):
        """Refreshes the services dictionary
        """
        self.location = location
        self.name = name
        self.device_group = device_group
        self.device_group_list = device_group_list
        if self.location.lower() == 'all':
            self._services_in_all()
        elif self.location.lower() in ['predefined', 'shared']:
            self._services_in_predefined_or_shared()
        elif self.location.lower() == 'device-group':
            self._services_in_device_groups()

    def _services_in_all(self):
        """Retrieves all services requires device group list to be defined
        """
        for loc in ['predefined', 'shared', 'device-group']:
            print(f"getting {loc}")
            if loc == 'device-group':
                self._services_in_device_groups_all()
            else:
                resp = get_restapi(device=self.device, api_key=self.api_key,
                                   device_group=loc, name=self.name, verify=self.
                                   certstore, url_type=self.url_type, version=self.version)
                self.services[loc] = resp.json()["result"]

    def _services_in_device_groups(self):
        """retrieves just the device groups either name defined or if a
         specific device group requested
        """
        if not self.device_group:
            raise PaloAltoMissingParam(f"missing device-group: {self.device_group}")
        if not self.services.get('device-group'):
            self.services['device-group'] = {}
        if self.name and self.device_group:
            resp = get_restapi(
                device=self.device, api_key=self.api_key, name=self.name,
                verify=self.certstore, url_type=self.url_type, version=self.version,
                device_group=self.device_group)
            self.services['device-group'][self.device_group] = resp.json()["result"]
        else:
            resp = get_restapi(
                device=self.device, api_key=self.api_key,
                verify=self.certstore, url_type=self.url_type, version=self.version,
                device_group=self.device_group)
            self.services['device-group'][self.device_group] = resp.json()["result"]

    def _services_in_device_groups_all(self):
        """Goes through entire list of device groups and pulls each services defined

        Raises:
            PaloAltoMissingParam: _description_
        """
        if not self.services.get('device-group'):
            self.services['device-group'] = {}
        #print(f"Device Group: {self.device_group_list}")
        if 'shared' in self.device_group_list:
            self.device_group_list.remove('shared')
        if self.device_group_list:
            for dev_grp in self.device_group_list:
                params = {}
                params['device'] = self.device
                params['api_key'] = self.api_key
                params['version'] = self.version
                params['url_type'] = self.url_type
                params['device_group'] = dev_grp
                params['certstore'] = self.certstore
                threads = []
                thr = threading.Thread(target=svc_thread_func, args=(params, self.services))
                threads.append(thr)
                thr.start()
            for index, thread in enumerate(threads):
                thread.join()
        else:
            raise PaloAltoMissingParam(
                "missing device-group parameter to get devicegroup services")

    def _services_in_predefined_or_shared(self):
        """Used to generate a services list used for predefined or shared location types
        """
        resp = get_restapi(device=self.device, api_key=self.api_key,
                           device_group=self.location, name=self.name, verify=self.
                           certstore, url_type=self.url_type, version=self.version)
        self.services[self.location] = resp.json()["result"]

def svc_thread_func(params: dict, results: dict):
    """Used for multithreading calls when multiple device groups are called

    Args:
        params (dict): _description_
        results (dict): _description_
    """
    print(f"getting {params['device_group']}")
    resp = get_restapi(
                    device=params['device'], api_key=params['api_key'],
                    verify=params['certstore'], url_type=params['url_type'], version=params['version'],
                    device_group=params['device_group'])
    results['device-group'][params['device_group']] = resp.json()["result"]
