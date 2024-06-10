#!/usr/bin/env python

from bandwidth_numbers.models.maps.base_map import BaseMap

class PortInsMap(BaseMap):

    links = None
    lnp_port_info_for_given_status = None
    total_count = None
