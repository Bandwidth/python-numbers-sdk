#!/usr/bin/env python

from bandwidth_numbers.models.data.address import Address
from bandwidth_numbers.models.data.calling_name import CallingName
from bandwidth_numbers.models.data.hosts import Hosts
from bandwidth_numbers.models.data.termination_hosts import TerminationHosts
from bandwidth_numbers.models.maps.sip_peer import SipPeerMap

class SipPeerData(SipPeerMap):

    @property
    def name(self):
        return self.peer_name
    @name.setter
    def name(self, name):
        self.peer_name = name

    def __init__(self):
        self.address = Address()
        self.calling_name = CallingName()
        self.sms_hosts = Hosts()
        self.termination_hosts = TerminationHosts()
        self.voice_hosts = Hosts()
