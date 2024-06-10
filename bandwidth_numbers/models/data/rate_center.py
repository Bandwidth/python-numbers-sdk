#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.cities_short_list import CitiesShortList
from bandwidth_numbers.models.data.local_rate_center_list import LocalRateCenterList
from bandwidth_numbers.models.data.npanxx_list import NpanxxList
from bandwidth_numbers.models.data.tier_list import TierList
from bandwidth_numbers.models.data.zip_code_list import ZipCodeList
from bandwidth_numbers.models.maps.rate_center import RateCenterMap

class RateCenterData(RateCenterMap, BaseData):

    def __init__(self):
        self.cities = CitiesShortList()
        self.local_rate_centers = LocalRateCenterList()
        self.npa_nxx_xs = NpanxxList()
        self.tiers = TierList()
        self.zip_codes = ZipCodeList()
