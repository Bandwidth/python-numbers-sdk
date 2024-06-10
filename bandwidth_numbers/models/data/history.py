#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.order_history import OrderHistoryData
from bandwidth_numbers.models.maps.history import HistoryMap

class HistoryData(HistoryMap, BaseData):

    def __init__(self):
        self.order_history = BaseResourceList(OrderHistoryData)
