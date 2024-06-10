#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.order_tns import OrderTnsMap

class OrderTnsData(OrderTnsMap, BaseData):

    def __init__(self):
        self.telephone_number = BaseResourceSimpleList()
