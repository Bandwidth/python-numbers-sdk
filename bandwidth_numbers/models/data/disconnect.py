#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.error_list import ErrorList
from bandwidth_numbers.models.data.disconnect_telephone_number_order_type import \
    DisconnectTelephoneNumberOrderType
from bandwidth_numbers.models.telephone_number import TelephoneNumber
from bandwidth_numbers.models.maps.disconnect import DisconnectMap

class DisconnectData(DisconnectMap, BaseData):

    @property
    def count_of_tns(self):
        return self.count_of_t_ns
    @count_of_tns.setter
    def count_of_tns(self, count_of_tns):
        self.count_of_t_ns = count_of_tns

    def __init__(self):
        self.disconnect_telephone_number_order_type = \
            DisconnectTelephoneNumberOrderType()
        self.telephone_number_details = TelephoneNumber()
