#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.sip_peer_telephone_numbers import \
    SipPeerTelephoneNumbers
from bandwidth_numbers.models.maps.sip_peer_tns import SipPeerTnsMap

class SipPeerTnsData(SipPeerTnsMap, BaseData):

    def __init__(self, parent=None):
        self.sip_peer_telephone_numbers = SipPeerTelephoneNumbers(parent)
