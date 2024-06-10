#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.data.full_numbers import FullNumbers
from bandwidth_numbers.models.maps.completed_numbers import CompletedNumbersMap

class CompletedNumbers(CompletedNumbersMap, BaseData):

    @property
    def items(self):
        return self.telephone_number.items

    def __init__(self):
        self.telephone_number = FullNumbers()

    def add(self, phone_number=None):
        return self.telephone_number.add(phone_number)
