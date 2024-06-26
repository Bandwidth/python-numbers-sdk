#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.tier_list import TierListMap

class TierList(TierListMap, BaseData):

    @property
    def items(self):
        return self.tier.items

    def __init__(self):
        self.tier = BaseResourceSimpleList()
