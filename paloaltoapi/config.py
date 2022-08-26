"""application config"""
import os

from paloaltoapi.statics import DEVICE_GRP_BASE

class Config:
    """
    Configuration untility
    """
    CERT = os.environ.get("CERT", False)
    DOMAIN = os.environ.get("DOMAIN", '')
    GLOBAL_SEARCHES = {
        # Get tag based off name
        'tags_xml': [
            {
                'xpath': '/config/devices//entry/device-group/*/tag/entry[@name="{}"]',
                'location-type': 'device-groups'
            },
            {
                'xpath': '/config/shared/tag/entry[@name="{}"]',
                'location-type': 'shared'
            }
        ],
        # Retrieve all tags
        'tags_all_xml': [
            {
                'xpath': '/config/devices//entry/device-group/*/tag',
                'location-type': 'device-groups'
            },
            {
                'xpath': '/config/shared/tag',
                'location-type': 'shared'
            }
        ],
        'addresses': [
            {
                'xpath': '/config/shared/address/entry[{}]',
                'location-type': 'shared'
            },
            {
                'xpath': '/config/devices//entry/device-group//entry/address/entry[{}]',
                'location-type': 'device-groups'
            }
        ],
        # Gets the Address using the Obj Name using XML Search
        'addresses_xml': [
            {
                'xpath': '/config/devices//entry/device-group/*/address/entry[@name="{}"]',
                'location-type': 'device-groups'
            },
            {
                'xpath': '/config/shared/address/entry[@name="{}"]',
                'location-type': 'shared'
            },

        ],
        'address-groups': [
            {
                'xpath': '/config/shared/address-group/entry[{}]',
                'location-type': 'shared',
                'location': 'shared'
            },
            {
                'xpath': '/config/devices//entry/device-group//entry/address-group/entry[{}]',
                'location-type': 'device-groups',
                'location': ''
            }
        ],
        # Gets the Address Group using the Obj Name using XML Search
        'address_groups_xml': [
             {
                'xpath': '/config/devices//entry/device-group/*/address-group/entry[@name="{}"]',
                'location-type': 'device-groups'
            },
            {
                'xpath': '/config/shared/address-group/entry[@name="{}"]',
                'location-type': 'shared'
            },

        ],
        'rules': [
            {
                'xpath': '/config/shared/*/*/rules/entry[{}]',
                'location-type': 'shared',
                'location': 'shared'
            },
            {
                'xpath': '/config/devices//entry/device-group//entry/*/security/rules/entry[{}]',
                'location-type': 'device-groups',
                'location': ''
            },
        ],
        'address-groups-search': [
            {
                'xpath': '/config/shared/address-group/entry[{}]',
                'location-type': 'shared',
                'location': 'shared'
            },
            {
                'xpath': '/config/devices//entry/device-group/entry[@name="{}"]'+
                          '/address-group/entry[{}]',
                'location-type': 'device-groups',
                'location': ''
            },
        ],
        'version': [
            {
                "request_type": "GET",
                "url": "https://{}/api",
                "params": {
                    "type": "op",
                    "cmd": "<show><system><info></info></system></show>"
                },
                "headers": {
                    "X-PAN-KEY": '{}'
                },
            }
        ],
        'nat': [
            {
                'xpath': '/config/shared/*/nat/rules/entry[{}]',
                'location-type': 'shared',
                'location': 'shared'
            },
            {
                'xpath': '/config/devices//entry/device-group/entry/*/nat/rules/entry[{}]',
                'location-type': 'device-group',
                'location': ''
            },
        ],
        'rule_location': {
            # Must fill with pre/post-rulebase and will search for any uuid in that field
            'xpath': '/config/devices//entry/device-group//'
                     'entry[{}/*/rules/entry[@uuid="{}"]]/@name'
        },
        'rule_location_shared': {
            'xpath': '/config/shared/{}/*/*/entry[@uuid="{}"]'
        },
    }
    REST_URLS = {
        # Requires backfill for version
        'addresses': '/Objects/Addresses',
        'address_groups': '/Objects/AddressGroups',
    }
    ADDRESS_GROUP = {
        # Required when adding an object
        'element': '<member>{}</member>',
        # Used to add or remove an obj from an address group
        'update': {
            'shared': '/config/shared/address-group/entry[@name="{}"]/static/member[text()="{}"]',
            'device-group': '/config/devices/entry[@name="localhost.localdomain"]/'+
                            'device-group/entry[@name="{}"]/address-group/entry[@name="{}"]'+
                            '/static/member[text()="{}"]'
        },
        'add': {
            'shared': '/config/shared/address-group/entry[@name="{}"]/static',
        }
    }
    URL_SEARCHES = {
        'url': "<test><url>{}</url></test>",
        'custom-url': "<test><custom-url><url>{}</url></custom-url></test>"
    }
    SECURITY_RULES = {
        # Starting with DECOM assigments
        'delete': {
            'shared': "/config/shared/{}/security/rules/entry[@name='{}']"+
                        "/{}/member[text()='{}']",
            'device-group': DEVICE_GRP_BASE +
                            "/device-group/entry[@name='{}']/{}/security/rules/entry[@name='{}']"+
                            "/{}/member[text()='{}']"
        },
        'set': {
            'shared': "/config/shared/{}/security/rules/entry[@name='{}']/{}",
            'device-group': DEVICE_GRP_BASE +
                            "/device-group/entry[@name='{}']/{}/security/rules/entry[@name='{}']"+
                            "/{}",
        }
    }
    POLICIES = {
        'audit': {
            'cmd': "<set><audit-comment><xpath>{}</xpath><comment>{}</comment>"+
                    "</audit-comment></set>",
            'shared': "/config/shared/{}/{}/rules/entry[@name='{}']",
            'device-group': DEVICE_GRP_BASE +
                            "/device-group/entry[@name='{}']/{}/{}/rules/entry[@name='{}']"
        }
    }
    COMMANDS = {
        'panorama_commit': '<commit></commit>',
        'device_commit': '<commit-all><shared-policy><device-group><entry name="{}"/>'+
                            '</device-group></shared-policy></commit-all>',
        'get_job': '<show><jobs><id>{}</id></jobs></show>',
        'commit_lock': {
            'show': '<show><commit-locks/></show>',
            'add': '<request><commit-lock><add><comment>{}</comment></add></commit-lock></request>',
            'remove': '<request><commit-lock><remove/></commit-lock></request>',
            'remove_admin': '<request><commit-lock><remove><admin>{}</admin></remove>'+
                            '</commit-lock></request>',
        },
        'commit_revert': {
            'all': '<revert><config/></revert>',
            'admin': '<revert><config><partial><admin><member>{}</member>'+
                        '</admin></partial></config></revert>',
        }
    }
