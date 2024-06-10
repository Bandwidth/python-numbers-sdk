#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.tier_list import TierList
from bandwidth_numbers.models.data.tn_list import TnList
from bandwidth_numbers.models.maps.lnp_rate_center import LnpRateCenterMap

class LnpRateCenter(LnpRateCenterMap, BaseData):

    def __init__(self):
        self.tiers = TierList()
        self.tn_list = TnList()
