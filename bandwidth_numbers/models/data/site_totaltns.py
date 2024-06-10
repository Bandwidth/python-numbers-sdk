#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.site_totaltns import SiteTotaltnsMap

class SiteTotaltnsData(SiteTotaltnsMap, BaseData):

    @property
    def count(self):
        return self.total_count
    @count.setter
    def count(self, count):
        self.total_count = count
