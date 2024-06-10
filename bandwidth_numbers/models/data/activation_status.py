#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.maps.activation_status import ActivationStatusMap

class ActivationStatusData(ActivationStatusMap, BaseData):

    def __init__(self):
        self.activated_telephone_numbers_list = TelephoneNumberList()
        self.not_yet_activated_telephone_numbers_list = TelephoneNumberList()
