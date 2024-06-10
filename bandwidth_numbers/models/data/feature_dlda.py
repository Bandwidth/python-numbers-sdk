#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.address import Address
from bandwidth_numbers.models.data.listing_name import ListingName
from bandwidth_numbers.models.maps.feature_dlda import FeatureDldaMap

class FeatureDlda(FeatureDldaMap, BaseData):

    def __init__(self):
        self.address = Address()
        self.listing_name = ListingName()
