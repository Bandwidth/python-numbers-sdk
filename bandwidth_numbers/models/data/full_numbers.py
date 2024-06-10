#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.full_numbers import FullNumbersMap

class FullNumbers(FullNumbersMap, BaseData):

    @property
    def items(self):
        return self.full_number.items

    def __init__(self):
        self.full_number = BaseResourceSimpleList()

    def add(self, phone_number=None):
        return self.full_number.add(phone_number)
