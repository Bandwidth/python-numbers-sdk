#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.tn_list import TnList
from bandwidth_numbers.models.maps.lnpchecker import LnpCheckerMap

class LnpCheckerData(LnpCheckerMap, BaseData):

    def __init__(self):
        self.tn_list = TnList()
