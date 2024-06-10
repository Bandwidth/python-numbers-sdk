#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.links import Links
from bandwidth_numbers.models.data.listing_name import ListingName
from bandwidth_numbers.models.maps.tns import TnsMap

class TnsData(TnsMap, BaseData):

    @property
    def result_count(self):
        return self.telephone_number_count
    @result_count.setter
    def result_count(self, result_count):
        self.telephone_number_count = result_count

    def __init__(self):
        self.links = Links()
