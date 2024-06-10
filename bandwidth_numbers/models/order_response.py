#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.order_response import OrderResponseData

XPATH_ORDER_RESPONSE = "/{}"

class OrderResponse(BaseResource, OrderResponseData):

    """Telephone numbers order response"""

    _xpath = XPATH_ORDER_RESPONSE

    @property
    def id(self):
        return self.order.order_id
    @id.setter
    def id(self, order_id):
        self.order.order_id = order_id

    @property
    def order(self):
        return self._order
    @order.setter
    def order(self, order):
        self._order = order

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        OrderResponseData.__init__(self)

    def get(self, id=None, params=None):
        return self._get_data((id or self.id), params=params)
