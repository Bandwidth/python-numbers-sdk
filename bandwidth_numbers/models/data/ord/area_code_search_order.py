#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.area_code_search_order import \
    AreaCodeSearchOrderMap

class AreaCodeSearchOrder(AreaCodeSearchOrderMap, BaseData):
    pass
