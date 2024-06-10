#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.rate_center import RateCenterData
from bandwidth_numbers.models.maps.rate_centers_list import RateCentersListMap

class RateCentersList(RateCentersListMap, BaseData):

    def __init__(self):
        self.rate_center = BaseResourceList(RateCenterData)
