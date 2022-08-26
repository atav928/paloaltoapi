"""Policy Entries Template"""
import json

class BaseRule:
    """Cleans Entry"""
    def __init__(self, kwargs: dict):
        self.clean_entry = {}
        self.clean_entry["location"] = kwargs["location"]
        self.clean_entry["@name"] = kwargs.get("@name")
        self.clean_entry["@uuid"] = kwargs.get("@uuid")
        # Does not always return otherwise is a yes/no value
        self.clean_entry["disabled"] = kwargs.get("disabled")
        self.clean_entry["rulebase"] = kwargs.get("rulebase")
        self.fix_location()

    def fix_location(self):
        """Appends the location-type params based off the location psecified"""
        if self.clean_entry['location'] != 'shared':
            self.clean_entry['location-type'] = 'device-group'
        else:
            self.clean_entry['location-type'] = 'shared'

class SecurityRule(BaseRule):
    """Used for base Security Rule"""
    def __init__(self, kwargs: dict):
        super().__init__(kwargs=kwargs)

class NatRule(BaseRule):
    """Cleans NAT Rule Entry
    NAT Rule

    Both the naming convention and the order of the parameters tries to closly
    match what is presented in the GUI.

    There are groupings of parameters that give hints to the sections that
    they contribute towards:

        * source_translation_<etc>
        * source_translation_fallback_<etc>
        * source_translation_static_<etc>
        * destination_translation_<etc>

    Args:
        name (str): Name of the rule
        description (str): The description
        nat_type (str): Type of NAT
        fromzone (list): From zones
        tozone (list): To zones
        to_interface (str): Egress interface from route lookup
        service (str): The service
        source (list): Source addresses
        destination (list): Destination addresses
        source_translation_type (str): Type of source address translation
        source_translation_address_type (str): Address type for Dynamic IP
            And Port or Dynamic IP source translation types
        source_translation_interface (str): Interface of the source address
            translation for Dynamic IP and Port source translation types
        source_translation_ip_address (str): IP address of the source address
            translation for Dynamic IP and Port source translation types
        source_translation_translated_addresses (list): Translated addresses
            of the source address translation for Dynamic IP And Port or
            Dynamic IP source translation types
        source_translation_fallback_type (str): Type of fallback for Dynamic IP
            source translation types
        source_translation_fallback_translated_addresses (list): Addresses for
            translated address types of fallback source translation
        source_translation_fallback_interface (str): The interface for the
            fallback source translation
        source_translation_fallback_ip_type (str): The type of the IP address
            for the fallback source translation IP address
        source_translation_fallback_ip_address (str): The IP address of the
            fallback source translation
        source_translation_static_translated_address (str): The IP address
            for the static source translation
        source_translation_static_bi_directional (bool): Allow reverse
            translation from translated address to original address
        destination_translated_address (str): Translated destination IP
            address
        destination_translated_port (int): Translated destination port number
        ha_binding (str): Device binding configuration in HA Active-Active mode
        disabled (bool): Disable this rule
        negate_target (bool): Target all but the listed target firewalls
            (applies to panorama/device groups only)
        target (list): Apply this policy to the listed firewalls only
            (applies to panorama/device groups only)
        tag (list): Administrative tags
        destination_dynamic_translated_address (str): (PAN-OS 8.1+) Dynamic
            destination translated address.
        destination_dynamic_translated_port (int): (PAN-OS 8.1+) Dynamic
            destination translated port.
        destination_dynamic_translated_distribution (str): (PAN-OS 8.1+) Dynamic
            destination translated distribution.
        uuid (str): (PAN-OS 9.0+) The UUID for this rule.
        group_tag (str): (PAN-OS 9.0+) The group tag.
    """
    def __init__(self, kwargs: dict):
        super().__init__(kwargs=kwargs)
        self.clean_entry['destination'] = kwargs["destination"]["member"]
        self.clean_entry["source"] = kwargs["source"]["member"]
        self.clean_entry['service'] = kwargs['service']
        self.clean_entry['tozone'] = kwargs['to']['member']
        self.clean_entry['fromzone'] = kwargs['from']['member']
        if kwargs.get('tag'):
            self.clean_entry['tag'] = kwargs['tag']['member']
        else:
            self.clean_entry['tag'] = None
        self.check_translations(kwargs)

    def check_translations(self, entry: dict):
        """Checks translations
        """
        # Set the Desination translations
        if (entry.get('destination-translation') or
                entry.get('dynamic-destination-translation')):
            self.check_destinations(entry=entry)
        else:
            self.default_destinations()
        # Set Source Translations
        if entry.get('source-translation'):
            self.check_sources(entry=entry)
        else:
            self.default_sources()

    def default_sources(self):
        """Sets the default key/value pairs for the rule"""
        self.clean_entry['source-translation'] = None

    def default_destinations(self):
        """Sets the default key/value pairs for the rule"""
        self.clean_entry['destination-translation'] = None
        self.clean_entry['dynamic-destination-translation'] = None

    def check_destinations(self, entry: dict):
        """Check Dest
        """
        dest = 'destination-translation'
        dyna = 'dynamic-destination-translation'
        if entry.get(dest):
            # Carries over the destination-translation field
            tmp = json.dumps(entry[dest])
            self.clean_entry[dest] = json.loads(tmp)
        elif entry.get(dyna):
            # Carries over the dynamic dest trans field
            tmp = json.dumps(entry[dyna])
            self.clean_entry[dyna] = json.loads(tmp)
        else:
            # Use this as a placeholder incase need to debug returns
            self.clean_entry[dest] = 'no'
            self.clean_entry[dyna] = 'no'

    def check_sources(self, entry: dict):
        """
        Creates the Source Translation Key/Dict pair if seen above
        """
        src_trans = 'source-translation'
        tmp = json.dumps(entry[src_trans])
        self.clean_entry[src_trans] = json.loads(tmp)
