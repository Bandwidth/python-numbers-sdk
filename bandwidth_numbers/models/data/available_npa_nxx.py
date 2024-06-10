#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.available_npa_nxx_list import AvailableNpaNxxList
from bandwidth_numbers.models.maps.available_npa_nxx import AvailableNpaNxxMap

class AvailableNpaNxxData(AvailableNpaNxxMap, BaseData):

    def __init__(self):
        self.available_npa_nxx_list = AvailableNpaNxxList()
