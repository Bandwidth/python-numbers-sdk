#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.listing_name import ListingNameMap

class ListingName(ListingNameMap, BaseData):
    pass
