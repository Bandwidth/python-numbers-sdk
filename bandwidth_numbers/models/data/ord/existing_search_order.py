#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.maps.ord.existing_search_order import \
    ExistingSearchOrderMap
from bandwidth_numbers.models.data.reservation_list import ReservationList

class ExistingSearchOrder(ExistingSearchOrderMap, BaseData):

    def __init__(self):
        self.reservation_id_list = ReservationList()
        self.telephone_number_list = TelephoneNumberList()
