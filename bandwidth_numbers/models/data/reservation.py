#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.reservation import ReservationMap

class ReservationData(ReservationMap, BaseData):

    @property
    def account(self):
        return self.account_id
    @account.setter
    def account(self, account):
        self.account_id = account
