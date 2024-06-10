#!/usr/bin/env python

from bandwidth_numbers.models.maps.base_map import BaseMap

class SiteHostMap(BaseMap):

    sip_peer_hosts = None
    site_id = None
