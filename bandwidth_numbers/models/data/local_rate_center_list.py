#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.local_rate_center_list import LocalRateCenterListMap

class LocalRateCenterList(LocalRateCenterListMap, BaseData):

    @property
    def items(self):
        return self.local_rate_center_id.items

    def __init__(self):
        self.local_rate_center_id = BaseResourceSimpleList()
