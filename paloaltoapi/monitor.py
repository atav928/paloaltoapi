"""Used to monitor devices built for fwupgrade cli"""
import os, sys

def set_ping(system):
    LINUX_PING = "ping -c 1 "
    WIN_PING = "ping -n 1 " 

def ping_response(ip):
    pass

def check_ip(ip):
    pass