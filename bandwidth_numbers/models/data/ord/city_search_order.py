#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.city_search_order import CitySearchOrderMap

class CitySearchOrder(CitySearchOrderMap, BaseData):
    pass
