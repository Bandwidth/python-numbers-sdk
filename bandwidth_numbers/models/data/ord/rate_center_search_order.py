#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.rate_center_search_order import \
    RateCenterSearchOrderMap

class RateCenterSearchOrder(RateCenterSearchOrderMap, BaseData):
    pass
