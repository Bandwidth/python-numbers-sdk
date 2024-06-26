#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.reservation_list import ReservationListMap

class ReservationList(ReservationListMap, BaseData):

    @property
    def items(self):
        return self.reservation_id.items

    def __init__(self):
        self.reservation_id = BaseResourceSimpleList()

    def add(self, id=None):
        return self.reservation_id.add(id)
