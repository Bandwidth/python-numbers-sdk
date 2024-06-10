#!/usr/bin/env python
  
from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.tn_option_order import TnOptionOrderMap
from bandwidth_numbers.models.data.error_list import ErrorList
from bandwidth_numbers.models.data.warnings import Warnings
from bandwidth_numbers.models.data.tn_option_order_groups import TnOptionOrderGroupsData

class TnOptionOrderData(TnOptionOrderMap, BaseData):

    def __init__(self):
        self.error_list = ErrorList()
        self.warnings = Warnings()
        self.tn_option_groups = TnOptionOrderGroupsData()
