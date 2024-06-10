#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.error_list import ErrorList
from bandwidth_numbers.models.data.full_numbers import FullNumbers
from bandwidth_numbers.models.data.completed_numbers import CompletedNumbers
from bandwidth_numbers.models.maps.order_response import OrderResponseMap

class OrderResponseData(OrderResponseMap, BaseData):

    def __init__(self):
        self.completed_numbers = CompletedNumbers()
        self.error_list = ErrorList()
        self.failed_numbers = FullNumbers()
