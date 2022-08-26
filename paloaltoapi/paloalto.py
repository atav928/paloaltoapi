"""Dataclasses"""
from dataclasses import dataclass
from paloaltoapi import config

@dataclass
class paloalto_system:
    #api_key: str = app.config.get("PA_KEY")
    #device_group_list: list = [] 
    def __init__(self, kwargs) -> None:
        self.sw_version: str = kwargs.get('sw-version')
        self.version: str = '.'.join(self.sw_version.split('.')[:-1])
        self.hostname: str = f"{kwargs.get('hostname')}{config.DOMAIN}"
        self.uptime: str = kwargs.get('uptime')
        self.serial: str = kwargs.get('serial')
        self.devicename: str = kwargs.get('devicename')
        self.ip_address: str = kwargs.get('ip-address')
        self.model: str = kwargs.get('model')

    def __repr__(self) -> str:
        attrs = str([x for x in self.__dict__])
        return "<paloaltoapi.paloalto.paloalto_system: > {} ".format(attrs)