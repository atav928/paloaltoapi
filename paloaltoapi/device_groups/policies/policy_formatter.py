"""Audit Format"""

import pandas as pd


class DeviceRule:
    def __init__(self, rule: dict, id: int):
        value = rule
        self.id = id
        self.rule = rule
        self.name = value.get('@name', None)
        self.uuid = value.get('@uuid', None)
        self.location = value.get('@location', None)
        self.device_group = value.get('@device-group', None)
        self.zone_from = value['from'].get('member', None)
        self.zone_to = value['to'].get('member', None)
        self.source = value['source'].get('member', None)
        self.source_user = value['source-user'].get('member', None)
        self.hip_profiles = None if not value.get(
            'hip-profiles', None) else value['hip-profiles'].get('member', None)
        self.destination = value['destination'].get('member', None)
        self.application = value['application'].get('member', None)
        self.service = value['service'].get('member', None)
        self.category = None if not value.get(
            'category', None) else value['category'].get(
            'member', None)
        self.action = value.get('action', None)
        self.description = None if not value.get(
            'description', None) else value.get(
            'description', None).split('\n')
        self.log_setting = value.get('log-setting', None)
        self.log_start = value.get('log-start', None)
        self.log_end = value.get('log-end', None)
        self.tag = None if not value.get(
            'tag', None) else value['tag'].get('member', None)
        self.negate_source = value.get('negate-source', None)
        self.negate_destination = value.get('negate-destination', None)
        self.option = value.get('option', None)
        self.target = value.get('target', None)
        self.group_tag = value.get('group-tag', None)
        # if no value is returned than assumption is 'NO'
        self.disabled = value.get('disabled', 'no')

        # Profile Settings Samples:
        # profile_settings dict: {'group': {'member': ['Default-User-Profile']}}
        # profile_settings dict: None
        self.profile_setting_dict = None if not value.get(
            'profile-setting', None) else value['profile-setting']
        profile_setting = get_profile_type(self.profile_setting_dict)
        if profile_setting == 'group':
            self.profile = ProfileGroup(self.profile_setting_dict)
        elif profile_setting == 'profiles':
            self.profile = ProfilePolicy(self.profile_setting_dict['profiles'])
        else:
            self.profile = ProfileSettings()
        # TODO: introduce or remove
        #self.get_review_policies()

    def __repr__(self) -> str:
        attrs = str(list(self.__dict__))
        return f"<fwaudit.formatter.DeviceRule: > {attrs} "

    def to_dict(self):
        """displays info into a dictionary

        Returns:
            _type_: dict
        """
        return self.__dict__

    # Policy used for other audit process
    #def get_review_policies(self):
    #    """Reviews policy to determine if a review is required
    #    in the rule being evaluated
    #    """
    #    for review in REVIEW_POLICIY_KEYS:
    #        setattr(self, review, 'yes' if self.rule.get(review) else 'no')


def get_profile_type(profile: dict):
    """
    Retreives and sets the profile type  
    Args:
        profile (dict): {'profiles': []} or {'group': {'member': ['Default-Server-Profile']}}
    Return:
        (str): 'group', 'profiles', None
    """
    # Needed becuase Palo Alto will return an emtpy
    # profile or group dict if None is selected
    if (not profile
        or (profile.get('profiles') and profile.get('group'))
            or profile.get('profiles') == [] or profile.get('profiles') == {} or profile.get('group') == {}):
        print(f"{profile=}")
        # time.sleep(10)
        return None
    if profile.get('profiles', None):
        return 'profiles'
    if profile.get('group', None):
        return 'group'
    raise ValueError(f"Unable to retrieve profile attributes from {profile}")


class ProfileSettings:
    """
    Set Profile to None
    """

    def __init__(self):
        self.profile_setting_group = None
        self.profile_setting = None
        self.profile_setting_url = None
        self.profile_setting_data = None
        self.profile_setting_file = None
        self.profile_setting_wild = None
        self.profile_setting_virus = None
        self.profile_setting_spy = None
        self.profile_setting_vul = None
        self.profile_setting_gtp = None
        self.profile_setting_sctp = None

    def to_dict(self):
        """Returns values as a Dictionary

        Returns:
            _type_: dictionary
        """
        return self.__dict__

    def __repr__(self) -> str:
        attrs = str(list(self.__dict__))
        return f"<fwaudit.formatter.ProfileSettings: > {attrs} "


class ProfileGroup(ProfileSettings):
    """
    Set Profile to the Group
    """

    def __init__(self, profile: dict):
        """ Takes in the profile settings dict and applies the proper settings
        Args:
            profile (dict): profile_settings dict: {'group': {'member': ['Default-User-Profile']}}
        """
        super().__init__()
        self.profile_setting_group = profile.get('member')
        self.profile_setting = 'group'

    def __repr__(self) -> str:
        attrs = str(list(self.__dict__))
        return f"<fwaudit.formatter.ProfileGroup: > {attrs} "


class ProfilePolicy(ProfileSettings):
    """
    Sets Profile to Profile settings
    """

    def __init__(self, profile: dict):
        """
        Set profile to profiles
        """
        super().__init__()
        self.profile_setting = 'profiles'
        self.profile_setting_url = None if not profile.get(
            'url-filtering', None) else profile['url-filtering'].get('member')
        self.profile_setting_data = None if not profile.get(
            'data-filtering', None) else profile['data-filtering'].get('member')
        self.profile_setting_file = None if not profile.get(
            'file-blocking', None) else profile['file-blocking'].get('member')
        self.profile_setting_wild = None if not profile.get(
            'wildfire-analysis', None) else profile['wildfire-analysis'].get('member')
        self.profile_setting_virus = None if not profile.get(
            'virus', None) else profile['virus'].get('member')
        self.profile_setting_spy = None if not profile.get(
            'spyware', None) else profile['spyware'].get('member')
        self.profile_setting_vul = None if not profile.get(
            'vulnerability', None) else profile['vulnerability'].get('member')
        self.profile_setting_gtp = None if not profile.get(
            'gtp', None) else profile['gtp'].get('member')
        self.profile_setting_sctp = None if not profile.get(
            'sctp', None) else profile['sctp'].get('member')

    def __repr__(self) -> str:
        attrs = str(list(self.__dict__))
        return f"<fwaudit.formatter.ProfilePolicy: > {attrs} "


# Testing
if __name__ == "__main__":
    value = {'@name': 'Test Rule', '@uuid': 'f0f12abf-f2ad-513c-a5a0-53249b4d20a', '@location': 'device-group', '@device-group': 'External', '@loc': 'External', 'profile-setting': {'group': {'member': ['Default-Profile']}}, 'target': {'negate': 'no'}, 'option': {'disable-server-response-inspection': 'no'}, 'from': {'member': ['Untrust']}, 'to': {'member': ['Trust']}, 'source': {'member': ['internal-networks']}, 'destination': {'member': ['global-active-directory']}, 'source-user': {'member': ['any']}, 'category': {'member': ['any']}, 'application': {'member': [
        'active-directory', 'app-ldap-ssl', 'dns', 'kerberos', 'ldap', 'ms-ds-smb', 'ms-netlogon', 'ms-win-dns', 'msrpc', 'netbios-dg', 'netbios-ns', 'ntp', 'ping', 'tcp-over-dns']}, 'service': {'member': ['application-default']}, 'action': 'allow', 'log-start': 'no', 'log-end': 'yes', 'description': 'Allows Active-Directory', 'negate-source': 'no', 'negate-destination': 'no', 'log-setting': 'Log', 'disabled': 'no', 'source-hip': {'member': ['any']}}
    bad_value = value = {'@name': 'Test Rule', '@uuid': 'f0f12abf-f2ad-513c-a5a0-53249b4d20a', '@location': 'device-group', '@device-group': 'External', '@loc': 'External', 'profile-setting': {'group': {}}, 'target': {'negate': 'no'}, 'option': {'disable-server-response-inspection': 'no'}, 'from': {'member': ['Untrust']}, 'to': {'member': ['Trust']}, 'source': {'member': ['internal-networks']}, 'destination': {'member': ['global-active-directory']}, 'source-user': {'member': ['any']}, 'category': {'member': ['any']}, 'application': {'member': [
        'active-directory', 'app-ldap-ssl', 'dns', 'kerberos', 'ldap', 'ms-ds-smb', 'ms-netlogon', 'ms-win-dns', 'msrpc', 'netbios-dg', 'netbios-ns', 'ntp', 'ping', 'tcp-over-dns']}, 'service': {'member': ['application-default']}, 'action': 'allow', 'log-start': 'no', 'log-end': 'yes', 'description': 'Allows Active-Directory', 'negate-source': 'no', 'negate-destination': 'no', 'log-setting': 'Log', 'disabled': 'no', 'source-hip': {'member': ['any']}}
    index = 2
    rule = DeviceRule(rule=value, id=index)
    rule_df = pd.DataFrame.from_dict([rule])
