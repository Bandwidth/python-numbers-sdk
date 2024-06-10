#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.phone_number_list import PhoneNumberListMap

class PhoneNumberList(PhoneNumberListMap, BaseData):

    @property
    def items(self):
        return self.phone_number.items

    def __init__(self):
        self.phone_number = BaseResourceSimpleList()

    def add(self, phone_number=None):
        return self.phone_number.add(phone_number)
