#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.movetns import MovetnsMap

class MovetnsData(MovetnsMap, BaseData):

    def __init__(self):
        self.full_number = BaseResourceSimpleList()

    def add(self, phone_number):
        return self.full_number.add(phone_number)
