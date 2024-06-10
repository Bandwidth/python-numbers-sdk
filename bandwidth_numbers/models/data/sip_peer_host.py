#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.hosts import Hosts
from bandwidth_numbers.models.data.termination_hosts import TerminationHosts
from bandwidth_numbers.models.maps.sip_peer_host import SipPeerHostMap

class SipPeerHost(SipPeerHostMap, BaseData):

    def __init__(self):
        self.sms_hosts = Hosts()
        self.termination_hosts = Hosts()
        self.voice_hosts = Hosts()
