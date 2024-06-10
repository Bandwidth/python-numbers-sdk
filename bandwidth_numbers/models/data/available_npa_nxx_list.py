#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.npa_nxx import NpaNxx
from bandwidth_numbers.models.maps.available_npa_nxx_list import AvailableNpaNxxListMap

class AvailableNpaNxxList(AvailableNpaNxxListMap, BaseData):

    @property
    def items(self):
        return self.available_npa_nxx.items

    def __init__(self):
        self.available_npa_nxx = BaseResourceList(NpaNxx)
