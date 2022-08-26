"""Firewall Unit Test"""
import unittest
from unittest import mock
import paloaltoapi.firewall

def mocked_token(*args, **kwargs):
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.content = str.encode(
                "<response status = 'success'><result><key>1234567890</key></result></response>")
            self.text = self.content
    return MockResponse()

def mocked_version(*args, **kwargs):
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.content = str.encode(
                """<response status="success">
                    <result>
                        <system>
                            <hostname>fw-sslvpn</hostname>
                            <ip-address>10.0.0.29</ip-address>
                            <public-ip-address>unknown</public-ip-address>
                            <netmask>255.255.255.0</netmask>
                            <default-gateway>10.0.0.1</default-gateway>
                            <is-dhcp>no</is-dhcp>
                            <ipv6-address>unknown</ipv6-address>
                            <ipv6-link-local-address>fe80::a66:1fff:fe01:4ba4/64</ipv6-link-local-address>
                            <ipv6-default-gateway></ipv6-default-gateway>
                            <mac-address>08:66:1f:01:4b:a4</mac-address>
                            <time>Wed Jan 19 11:30:17 2022
                </time>
                            <uptime>77 days, 15:03:57</uptime>
                            <devicename>fw-sslvpn</devicename>
                            <family>5200</family>
                            <model>PA-5250</model>
                            <serial>013101005411</serial>
                            <cloud-mode>non-cloud</cloud-mode>
                            <sw-version>9.1.11</sw-version>
                            <global-protect-client-package-version>5.2.9</global-protect-client-package-version>
                            <app-version>8515-7181</app-version>
                            <app-release-date>2022/01/14 18:49:38 EST</app-release-date>
                            <av-version>3967-4478</av-version>
                            <av-release-date>2022/01/19 07:03:52 EST</av-release-date>
                            <threat-version>8515-7181</threat-version>
                            <threat-release-date>2022/01/14 18:49:38 EST</threat-release-date>
                            <wf-private-version>0</wf-private-version>
                            <wf-private-release-date>unknown</wf-private-release-date>
                            <url-db>paloaltonetworks</url-db>
                            <wildfire-version>630348-633567</wildfire-version>
                            <wildfire-release-date>2022/01/19 11:15:20 EST</wildfire-release-date>
                            <url-filtering-version>20220119.20247</url-filtering-version>
                            <global-protect-datafile-version>1604760636</global-protect-datafile-version>
                            <global-protect-datafile-release-date>2020/11/07 09:50:36</global-protect-datafile-release-date>
                            <global-protect-clientless-vpn-version>0</global-protect-clientless-vpn-version>
                            <global-protect-clientless-vpn-release-date></global-protect-clientless-vpn-release-date>
                            <logdb-version>9.1.22</logdb-version>
                            <platform-family>5200</platform-family>
                            <high-speed-log-forwarding-mode>off</high-speed-log-forwarding-mode>
                            <vpn-disable-mode>off</vpn-disable-mode>
                            <multi-vsys>on</multi-vsys>
                            <operational-mode>normal</operational-mode>
                            <device-certificate-status>None</device-certificate-status>
                        </system>
                    </result>
                </response>""")
            self.text = self.content
    return MockResponse()

def mocked_ha(*args, **kwargs):
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.content = str.encode(
                """<response status="success">
                    <result>
                        <enabled>yes</enabled>
                        <group>
                            <mode>Active-Passive</mode>
                            <local-info>
                                <url-compat>Mismatch</url-compat>
                                <app-version>8515-7181</app-version>
                                <gpclient-version>5.2.9</gpclient-version>
                                <build-rel>9.1.11</build-rel>
                                <ha2-port>hsci</ha2-port>
                                <av-version>3967-4478</av-version>
                                <url-version>20220119.20242</url-version>
                                <ha1-backup-ipaddr>192.168.253.1/24</ha1-backup-ipaddr>
                                <active-passive>
                                    <passive-link-state>auto</passive-link-state>
                                    <monitor-fail-holddown>1</monitor-fail-holddown>
                                </active-passive>
                                <platform-model>PA-5250</platform-model>
                                <av-compat>Match</av-compat>
                                <ha2-ipaddr>192.168.254.1/24</ha2-ipaddr>
                                <vpnclient-compat>Match</vpnclient-compat>
                                <ha1-ipaddr>192.168.255.1/24</ha1-ipaddr>
                                <ha1-backup-macaddr>08:66:1f:01:4e:36</ha1-backup-macaddr>
                                <vpnclient-version>Not Installed</vpnclient-version>
                                <ha2-macaddr>e8:98:6d:f0:17:08</ha2-macaddr>
                                <monitor-fail-holdup>0</monitor-fail-holdup>
                                <priority>100</priority>
                                <preempt-hold>1</preempt-hold>
                                <state>active</state>
                                <version>1</version>
                                <promotion-hold>2000</promotion-hold>
                                <threat-compat>Match</threat-compat>
                                <state-sync>Complete</state-sync>
                                <vm-license-compat>Match</vm-license-compat>
                                <addon-master-holdup>500</addon-master-holdup>
                                <heartbeat-interval>1000</heartbeat-interval>
                                <ha1-link-mon-intv>3000</ha1-link-mon-intv>
                                <hello-interval>8000</hello-interval>
                                <ha1-port>ha1-a</ha1-port>
                                <ha1-encrypt-imported>no</ha1-encrypt-imported>
                                <mgmt-ip>10.12.152.34/25</mgmt-ip>
                                <ha1-backup-port>ha1-b</ha1-backup-port>
                                <preempt-flap-cnt>0</preempt-flap-cnt>
                                <nonfunc-flap-cnt>0</nonfunc-flap-cnt>
                                <threat-version>8515-7181</threat-version>
                                <ha1-macaddr>08:66:1f:01:4e:37</ha1-macaddr>
                                <vm-license-type>Not Installed</vm-license-type>
                                <state-duration>7137025</state-duration>
                                <max-flaps>3</max-flaps>
                                <ha1-encrypt-enable>no</ha1-encrypt-enable>
                                <mgmt-ipv6></mgmt-ipv6>
                                <state-sync-type>ethernet</state-sync-type>
                                <preemptive>no</preemptive>
                                <gpclient-compat>Match</gpclient-compat>
                                <mode>Active-Passive</mode>
                                <build-compat>Match</build-compat>
                                <app-compat>Match</app-compat>
                            </local-info>
                            <peer-info>
                                <app-version>8515-7181</app-version>
                                <gpclient-version>5.2.9</gpclient-version>
                                <url-version>20211029.20023</url-version>
                                <ha1-backup-ipaddr>192.168.253.2</ha1-backup-ipaddr>
                                <av-version>3967-4478</av-version>
                                <platform-model>PA-5250</platform-model>
                                <ha2-ipaddr>192.168.254.2</ha2-ipaddr>
                                <ha1-ipaddr>192.168.255.2</ha1-ipaddr>
                                <vm-license></vm-license>
                                <ha2-macaddr>e8:98:6d:30:a6:08</ha2-macaddr>
                                <priority>100</priority>
                                <state>passive</state>
                                <version>1</version>
                                <last-error-reason>Link down</last-error-reason>
                                <build-rel>9.1.11</build-rel>
                                <conn-status>up</conn-status>
                                <ha1-backup-macaddr>08:66:1f:01:02:ac</ha1-backup-macaddr>
                                <vpnclient-version>Not Installed</vpnclient-version>
                                <mgmt-ip>10.12.152.26/25</mgmt-ip>
                                <conn-ha2>
                                    <conn-status>up</conn-status>
                                    <conn-ka-enbled>no</conn-ka-enbled>
                                    <conn-primary>yes</conn-primary>
                                    <conn-desc>link status</conn-desc>
                                </conn-ha2>
                                <threat-version>8515-7181</threat-version>
                                <ha1-macaddr>08:66:1f:01:02:ad</ha1-macaddr>
                                <conn-ha1>
                                    <conn-status>up</conn-status>
                                    <conn-primary>yes</conn-primary>
                                    <conn-desc>heartbeat status</conn-desc>
                                </conn-ha1>
                                <vm-license-type>Not Installed</vm-license-type>
                                <state-duration>2824844</state-duration>
                                <mgmt-ipv6></mgmt-ipv6>
                                <last-error-state>non-functional</last-error-state>
                                <preemptive>no</preemptive>
                                <mode>Active-Passive</mode>
                                <conn-ha1-backup>
                                    <conn-status>up</conn-status>
                                    <conn-desc>heartbeat status</conn-desc>
                                </conn-ha1-backup>
                            </peer-info>
                            <link-monitoring>
                                <fail-cond>any</fail-cond>
                                <enabled>no</enabled>
                                <groups>
                                    <entry>
                                        <interface/>
                                        <fail-cond>any</fail-cond>
                                        <enabled>no</enabled>
                                        <name>Monitor</name>
                                    </entry>
                                </groups>
                            </link-monitoring>
                            <path-monitoring>
                                <vwire/>
                                <fail-cond>any</fail-cond>
                                <vlan/>
                                <enabled>no</enabled>
                                <vrouter/>
                            </path-monitoring>
                            <running-sync>synchronized</running-sync>
                            <running-sync-enabled>yes</running-sync-enabled>
                        </group>
                    </result>
                </response>""")
            self.text = self.content
    return MockResponse()

class TestFirewall(unittest.TestCase):
    """Test Firewall Module"""
    @mock.patch("paloaltoapi.urls.ApiCalls.request",
                side_effect=[mocked_token(),mocked_ha(),mocked_version()])
    def test_firewall(self, mock):
        """Tests Firewall Class Object

        Args:
            mock ([type]): [description]
        """
        frwll = paloaltoapi.firewall.Firewall('example.com','admin','admin')
        self.assertEqual('example.com',frwll.device)
        self.assertEqual('1234567890',frwll.api_key)
        self.assertEqual('9.1',frwll.version)
        self.assertEqual('9.1.11',frwll.sw_version)
        self.assertEqual('yes',frwll.high_avail.ha_enabled)
