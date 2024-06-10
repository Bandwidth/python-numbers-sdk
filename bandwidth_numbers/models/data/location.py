#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.tn_rate_centers_list import TnRateCentersList
from bandwidth_numbers.models.maps.location import LocationMap

class Location(LocationMap, BaseData):

    def __init__(self):
        self.rate_centers = BaseResourceList(TnRateCentersList)
