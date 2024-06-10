#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.wildcard_search_order import \
    WildcardSearchOrderMap

class WildcardSearchOrder(WildcardSearchOrderMap, BaseData):
    pass
