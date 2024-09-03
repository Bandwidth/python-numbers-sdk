#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.tndetails import TndetailsData
from bandwidth_numbers.models.messaging_settings import MessagingSettings
from bandwidth_numbers.models.site import Site
from bandwidth_numbers.models.sip_peer import SipPeer

XML_NAME_TNDETAILS = "TelephoneNumberDetails"
XPATH_TNDETAILS = "/tndetails"

class Tndetails(BaseResource, TndetailsData):

    """Telephone number details"""

    _node_name = XML_NAME_TNDETAILS
    _xpath = XPATH_TNDETAILS

    @property
    def site(self):
        return self._site
    @site.setter
    def site(self, site):
        self._site = site

    @property
    def sip_peer(self):
        return self._sip_peer
    @sip_peer.setter
    def sip_peer(self, sip_peer):
        self._sip_peer = sip_peer

    @property
    def messaging_settings(self):
        return self._messaging_settings
    @messaging_settings.setter
    def messaging_settings(self, messaging_settings):
        self._messaging_settings = messaging_settings

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TndetailsData.__init__(self)
        self._site = Site(self, client)
        self._sip_peer = SipPeer(self, client)
        self._messaging_settings = MessagingSettings(self, client)


    def get(self):
        return self._get_data()
