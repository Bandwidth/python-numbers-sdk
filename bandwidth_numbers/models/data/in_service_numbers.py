#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.links import Links
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.maps.in_service_numbers import InServiceNumbersMap

class InServiceNumbersData(InServiceNumbersMap, BaseData):

    def __init__(self):
        self.links = Links()
        self.telephone_numbers = TelephoneNumberList()
