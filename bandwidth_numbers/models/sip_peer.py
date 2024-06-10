#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.sip_peer import SipPeerData
from bandwidth_numbers.models.data.address import Address
from bandwidth_numbers.models.data.calling_name import CallingName
from bandwidth_numbers.models.data.hosts import Hosts
from bandwidth_numbers.models.data.termination_hosts import TerminationHosts
from bandwidth_numbers.models.maps.sip_peer import SipPeerMap
from bandwidth_numbers.models.movetns import Movetns
from bandwidth_numbers.models.sip_peer_tns import SipPeerTns
from bandwidth_numbers.models.sip_peer_totaltns import SipPeerTotaltns

XPATH_SIP_PEER = "/{}"

class SipPeer(BaseResource, SipPeerData):

    """Site SIP peer"""

    _xpath = XPATH_SIP_PEER

    @property
    def id(self):
        return self.peer_id
    @id.setter
    def id(self, id):
        self.peer_id = id

    @property
    def movetns(self):
        return self._movetns

    @property
    def tns(self):
        return self._tns

    @property
    def totaltns(self):
        return self._totaltns

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SipPeerData.__init__(self)
        self._movetns = Movetns(self, client)
        self._tns = SipPeerTns(self, client)
        self._totaltns = SipPeerTotaltns(self, client)

    def get(self, id=None):
        return self._get_data(id)
