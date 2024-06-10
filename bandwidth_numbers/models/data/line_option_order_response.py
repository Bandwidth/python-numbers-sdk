#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.line_option_order_response import LineOptionOrderResponseMap
from bandwidth_numbers.models.data.line_options import LineOptionsData

class LineOptionOrderResponseData(LineOptionOrderResponseMap, BaseData):

    def __init__(self):
        self.line_options = BaseResourceList(LineOptionsData)
