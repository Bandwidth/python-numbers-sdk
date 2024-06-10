#!/usr/bin/env python

from bandwidth_numbers.models.maps.base_map import BaseMap

class CoveredRateCentersMap(BaseMap):

    links = None
    covered_rate_center = None
    total_count = None
