#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.npa_search_order import NpaSearchOrderMap

class NpaSearchOrder(NpaSearchOrderMap, BaseData):
    pass
