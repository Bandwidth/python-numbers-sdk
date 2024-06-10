#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource, BaseResourceList
from bandwidth_numbers.models.data.site import SiteData
from bandwidth_numbers.models.orders import Orders
from bandwidth_numbers.models.portins import PortIns
from bandwidth_numbers.models.sip_peers import SipPeers
from bandwidth_numbers.models.site_totaltns import SiteTotaltns


XPATH_SITE = "/{}"

class Site(BaseResource, SiteData):

    """Account site"""

    _xpath = XPATH_SITE

    @property
    def orders(self):
        return self._orders

    @property
    def portins(self):
        return self._portins

    @property
    def sip_peers(self):
        return self._sip_peers

    @property
    def totaltns(self):
        return self._totaltns

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SiteData.__init__(self)
        self._orders = Orders(self, client)
        self._portins = PortIns(self, client)
        self._sip_peers = SipPeers(self, client)
        self._totaltns = SiteTotaltns(self, client)

    def get(self, id=None):
        return self._get_data(id)
