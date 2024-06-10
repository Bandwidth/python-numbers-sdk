#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.include.xml_consts import XML_PARAM_TN_DETAIL, XML_TRUE
from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.available_numbers import AvailableNumbersData

XML_NAME_AVAILABLE_NUMBERS = "SearchResult"
XPATH_AVAILABLE_NUMBERS = "/availableNumbers"

class AvailableNumbers(BaseResource, AvailableNumbersData):

    """Available numbers for account"""

    _node_name = XML_NAME_AVAILABLE_NUMBERS
    _xpath = XPATH_AVAILABLE_NUMBERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        AvailableNumbersData.__init__(self)

    def list(self, params):
        self.get(params=params)
        if params.get(XML_PARAM_TN_DETAIL, "") == XML_TRUE:
            return self.telephone_number_detail_list.telephone_number_detail
        else:
            return self.telephone_number_list.telephone_number
