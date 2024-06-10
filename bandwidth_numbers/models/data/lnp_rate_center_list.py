#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.lnp_rate_center import LnpRateCenter
from bandwidth_numbers.models.maps.lnp_rate_center_list import LnpRateCenterListMap

class LnpRateCenterList(LnpRateCenterListMap, BaseData):

    @property
    def items(self):
        return self.rate_center_group.items

    def __init__(self):
        self.rate_center_group = BaseResourceList(LnpRateCenter)
