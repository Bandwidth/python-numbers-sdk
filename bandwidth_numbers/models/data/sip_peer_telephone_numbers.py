#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.sip_peer_telephone_numbers import \
    SipPeerTelephoneNumbersMap
from bandwidth_numbers.models.sip_peer_telephone_number import \
    SipPeerTelephoneNumber

class SipPeerTelephoneNumbers(SipPeerTelephoneNumbersMap, BaseData):

    @property
    def items(self):
        return self.sip_peer_telephone_number.items

    def __init__(self, parent=None):
        self.sip_peer_telephone_number = BaseResourceList(
            SipPeerTelephoneNumber, parent)
