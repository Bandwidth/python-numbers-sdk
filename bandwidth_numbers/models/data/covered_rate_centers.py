#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.links import Links
from bandwidth_numbers.models.rate_center import RateCenter
from bandwidth_numbers.models.maps.covered_rate_centers import CoveredRateCentersMap

class CoveredRateCentersData(CoveredRateCentersMap, BaseData):

    def __init__(self, parent=None):
        self.links = Links()
        self.covered_rate_center = BaseResourceList(RateCenter, parent)
