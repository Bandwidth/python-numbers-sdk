#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.tn_rate_center import TnRateCenterMap

class TnRateCenterData(TnRateCenterMap, BaseData):

    @property
    def name(self):
        return self.rate_center
    @name.setter
    def name(self, name):
        self.rate_center = name
