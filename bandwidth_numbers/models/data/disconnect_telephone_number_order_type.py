#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.maps.disconnect_telephone_number_order_type import \
    DisconnectTelephoneNumberOrderTypeMap

class DisconnectTelephoneNumberOrderType(
        DisconnectTelephoneNumberOrderTypeMap, BaseData):

    def __init__(self):
        self.telephone_number_list = TelephoneNumberList()
