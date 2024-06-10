#!/usr/bin/env python

from bandwidth_numbers.models.maps.base_map import BaseMap

class SipPeerHostMap(BaseMap):

    sip_peer_id = None
    sms_hosts = None
    termination_hosts = None
    voice_hosts = None
