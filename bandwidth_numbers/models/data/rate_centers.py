#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.rate_centers_list import RateCentersList
from bandwidth_numbers.models.maps.rate_centers import RateCentersMap

class RateCentersData(RateCentersMap, BaseData):

    @property
    def total_count(self):
        return self.result_count
    @total_count.setter
    def total_count(self, total_count):
        self.result_count = total_count

    def __init__(self):
        self.rate_centers = RateCentersList()
