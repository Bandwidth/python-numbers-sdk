#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.links import Links
from bandwidth_numbers.models.maps.orders import OrdersMap
from bandwidth_numbers.models.order import Order

class OrdersData(OrdersMap, BaseData):

    def __init__(self, parent=None):
        self.links = Links()
        self.order_id_user_id_date = BaseResourceList(Order, parent)
