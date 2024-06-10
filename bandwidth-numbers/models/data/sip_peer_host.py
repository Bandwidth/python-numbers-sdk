#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.hosts import Hosts
from iris_sdk.models.data.termination_hosts import TerminationHosts
from iris_sdk.models.maps.sip_peer_host import SipPeerHostMap

class SipPeerHost(SipPeerHostMap, BaseData):

    def __init__(self):
        self.sms_hosts = Hosts()
        self.termination_hosts = Hosts()
        self.voice_hosts = Hosts()