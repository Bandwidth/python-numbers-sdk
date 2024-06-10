#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.npanxx_list import NpanxxListMap

class NpanxxList(NpanxxListMap, BaseData):

    @property
    def items(self):
        return self.npanxx.items

    @property
    def npa_nxx_x(self):
        return self.npanxx

    def __init__(self):
        self.npanxx = BaseResourceSimpleList()
