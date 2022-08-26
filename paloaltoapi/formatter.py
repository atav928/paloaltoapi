"""formatter"""

from dataclasses import dataclass
from xml.etree import ElementTree as ET

from requests.models import Response

from paloaltoapi.test_data import PANORAMA_DAG_XML


@dataclass
class DYNAMIC_ADDRESS_GROUP:
    def __init__(self, response: dict):
        pass


def extract_registered_ip(xml: Response):
    ip_list = []
    root = ET.fromstring(xml.content)
    for child in root.iter('*'):
        if child.attrib.get('ip'):
            ip_list.append(child.attrib['ip'])
    #not_none_values = filter(None.__ne__, ip_list)
    # return list(not_none_values)
    return ip_list


# testing xml

if __name__ == '__main__':

    pa_root = ET.fromstring(PANORAMA_DAG_XML)
    for child in pa_root.iter('entry'):
        print(child.tag, child.attrib)

    # Get the device groups
    device_groups = []
    for child in pa_root.iter('entry'):
        device_groups.append(child.attrib['name'])
    print(device_groups)
