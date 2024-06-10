#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.order_history import OrderHistoryMap

class OrderHistoryData(OrderHistoryMap, BaseData):
    pass
