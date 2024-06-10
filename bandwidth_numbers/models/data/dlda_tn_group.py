#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.dlda_tn_group import DldaTnGroupMap
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.data.address import Address
from bandwidth_numbers.models.data.listing_name import ListingName

class DldaTnGroupData(DldaTnGroupMap, BaseData):

    def __init__(self):
        self.telephone_numbers = TelephoneNumberList()
        self.listing_name = ListingName()
        self.address = Address()
