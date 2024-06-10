#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.telephone_number_list import TelephoneNumberListMap

class TelephoneNumberList(TelephoneNumberListMap, BaseData):

    @property
    def items(self):
        return self.telephone_number.items

    def __init__(self):
        self.telephone_number = BaseResourceSimpleList()

    def add(self, phone_number=None):
        return self.telephone_number.add(phone_number)
