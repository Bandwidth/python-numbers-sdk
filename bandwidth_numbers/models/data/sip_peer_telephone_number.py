#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.tn_attributes import TnAttributes
from bandwidth_numbers.models.maps.sip_peer_telephone_number import \
    SipPeerTelephoneNumberMap

class SipPeerTelephoneNumberData(SipPeerTelephoneNumberMap, BaseData):

    def __init__(self):
        self.tn_attributes = TnAttributes()
