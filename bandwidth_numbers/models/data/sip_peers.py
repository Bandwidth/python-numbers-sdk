#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.sip_peers import SipPeersMap
from bandwidth_numbers.models.sip_peer import SipPeer

class SipPeersData(SipPeersMap, BaseData):

    def __init__(self, parent=None):
        self.sip_peer = BaseResourceList(SipPeer, self)
