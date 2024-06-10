#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.error import Error
from bandwidth_numbers.models.data.phone_number_list import PhoneNumberList
from bandwidth_numbers.models.data.subscriber import Subscriber
from bandwidth_numbers.models.data.wireless_info import WirelessInfo
from bandwidth_numbers.models.maps.portin import PortInMap

class PortInData(PortInMap, BaseData):

    @property
    def count_of_tns(self):
        return self.count_of_t_ns
    @count_of_tns.setter
    def count_of_tns(self, count_of_tns):
        self.count_of_t_ns = count_of_tns

    def __init__(self):
        self.errors = Error()
        self.list_of_phone_numbers = PhoneNumberList()
        self.status = Error()
        self.subscriber = Subscriber()
        self.wireless_info = WirelessInfo()

    def add_tn(self, number):
        return self.list_of_phone_numbers.items.add(number)
