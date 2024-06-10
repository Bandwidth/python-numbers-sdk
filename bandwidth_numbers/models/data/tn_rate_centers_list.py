#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.data.tn_rc_list import TelephoneNumberRcList
from bandwidth_numbers.models.maps.tn_rate_centers_list import TnRateCentersListMap

class TnRateCentersList(TnRateCentersListMap, BaseData):

    @property
    def items(self):
        return self.rcs.items

    @property
    def rcs(self):
        return self.r_cs

    def __init__(self):
        self.r_cs = TelephoneNumberRcList()
