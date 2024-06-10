#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.line_option_order import LineOptionOrderMap
from bandwidth_numbers.models.data.tn_line_options import TnLineOptionsData

class LineOptionOrderData(LineOptionOrderMap, BaseData):

    def __init__(self, parent=None):
        self.tn_line_options = BaseResourceList(TnLineOptionsData)
