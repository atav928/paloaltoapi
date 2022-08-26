"""Static Values"""
FW_ATTR = ['hostname', 'ip_address', 'default_gateway', 'sw_version', 
            'serial', 'model', 'device_certificate', 'devicename', 
            'uptime', 'time', 'device']

HA_ATTR = ['ha_enabled', 'ha_running_sync', 'ha_local_priority', 
        'ha_local_state', 'ha_local_preemtive', 'ha_local_sync_running', 
        'ha_local_sync_enabled', 'ha_peer_ip', 'ha_peer_state', 'ha_suspend_state']

DEVICEGROUP_ATTR = [
        "objects", "policy"
]
SECURITY_RULES = [
        "PreRules", "PostRules"
]
POLICY_ATTR = [
        "@name", "@uuid", "@location", "from", "to", "source",
        "destination", "source-user", "category"
]

RULEBASE = [
        "pre-rulebase", "post-rulebase"
]

DEVICE_GRP_BASE = "/config/devices/entry[@name='localhost.localdomain']"

RESTAPI_BASEURL = "https://{}/restapi/{}"
RESTAPI_BASEURL_V = "https://{}/restapi/v{}"
XML_BASEURL = "https://{}/api"

BASEURL = {
        '9.0': RESTAPI_BASEURL,
        'xml': XML_BASEURL,
        '9.1': RESTAPI_BASEURL_V,
        '10.0': RESTAPI_BASEURL_V,
        'latest': RESTAPI_BASEURL_V
}

PARSER = 'html.parser'
