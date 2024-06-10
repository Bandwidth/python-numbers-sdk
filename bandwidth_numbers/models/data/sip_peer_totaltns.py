#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.sip_peer_totaltns import SipPeerTotaltnsMap

class SipPeerTotaltnsData(SipPeerTotaltnsMap, BaseData):

    @property
    def count(self):
        return self.sip_peer_telephone_numbers_count
    @count.setter
    def count(self, count):
        self.sip_peer_telephone_numbers_count = count
