#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.vanity_search_order import \
    VanitySearchOrderMap

class VanitySearchOrder(VanitySearchOrderMap, BaseData):
    pass
