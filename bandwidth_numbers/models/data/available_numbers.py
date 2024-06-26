#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.data.telephone_number_detail_list import \
    TelephoneNumberDetailList
from bandwidth_numbers.models.maps.available_numbers import AvailableNumbersMap

class AvailableNumbersData(AvailableNumbersMap):

    @property
    def total_count(self):
        return self.result_count
    @total_count.setter
    def total_count(self, total_count):
        self.result_count = total_count

    def __init__(self):
        self.telephone_number_detail_list = TelephoneNumberDetailList()
        self.telephone_number_list = TelephoneNumberList()
