#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.sip_peer_hosts import SipPeerHosts
from bandwidth_numbers.models.maps.site_host import SiteHostMap

class SiteHost(SiteHostMap, BaseData):

    def __init__(self):
        self.sip_peer_hosts = SipPeerHosts()
