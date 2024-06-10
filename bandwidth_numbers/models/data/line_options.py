#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.line_options import LineOptionsMap
from bandwidth_numbers.models.data.error_list import ErrorList
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList

class LineOptionsData(LineOptionsMap, BaseData):

    def __init__(self, parent=None):
        self.complete_numbers = TelephoneNumberList()
        self.errors = ErrorList()
