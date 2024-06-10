#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.sip_peer_host import SipPeerHost
from bandwidth_numbers.models.maps.sip_peer_hosts import SipPeerHostsMap

class SipPeerHosts(SipPeerHostsMap, BaseData):

    @property
    def items(self):
        return self.sip_peer_host.items

    def __init__(self):
        self.sip_peer_host = BaseResourceList(SipPeerHost)
