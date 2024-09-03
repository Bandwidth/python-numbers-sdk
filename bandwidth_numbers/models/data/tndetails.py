#!/usr/bin/env python
from traceback import print_last

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.features import Features
from bandwidth_numbers.models.data.site import SiteData
from bandwidth_numbers.models.data.sip_peer import SipPeerData
from bandwidth_numbers.models.maps.tndetails import TndetailsMap
from bandwidth_numbers.models.data.messaging_settings import MessagingSettingsData


class TndetailsData(TndetailsMap, BaseData):

    @property
    def id(self):
        return self.full_number
    @id.setter
    def id(self, id):
        self.full_number = id

    @property
    def site(self):
        return self.site
    @site.setter
    def site(self, site):
        self.site = site

    @property
    def sip_peer(self):
        return self._sip_peer
    @sip_peer.setter
    def sip_peer(self, sip_peer):
        self._sip_peer = sip_peer


    @property
    def messaging_settings(self):
        return self.messaging_settings
    @messaging_settings.setter
    def messaging_settings(self, messaging_settings):
        self.messaging_settings = messaging_settings

    @property
    def last_modified_date(self):
        return self.last_modified
    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        self.last_modified = last_modified_date

    def __init__(self):
        self.features = Features()
        self.site = SiteData()
        self.sip_peer = SipPeerData()
        self.messaging_settings = MessagingSettingsData()

    @messaging_settings.setter
    def messaging_settings(self, value):
        self._messaging_settings = value
