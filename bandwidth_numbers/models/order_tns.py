#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource, BaseResourceList
from bandwidth_numbers.models.data.order_tns import OrderTnsData

XML_NAME_TNS_ORDERS = "TelephoneNumbers"
XPATH_TNS_ORDERS = "/tns"

class OrderTns(BaseResource, OrderTnsData):

    """Telephone numbers directory"""

    _node_name = XML_NAME_TNS_ORDERS
    _xpath = XPATH_TNS_ORDERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        OrderTnsData.__init__(self)

    def list(self):
        return self._get_data().telephone_number
