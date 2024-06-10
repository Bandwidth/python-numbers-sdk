#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.zip_search_order import \
    ZipSearchOrderMap

class ZipSearchOrder(ZipSearchOrderMap, BaseData):
    pass
