#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.tn_option_order_groups import TnOptionOrderGroupsMap
from bandwidth_numbers.models.data.tn_option_order_group import TnOptionOrderGroupData

class TnOptionOrderGroupsData(TnOptionOrderGroupsMap, BaseData):

    def __init__(self, parent=None):
        self.tn_option_group = BaseResourceList(TnOptionOrderGroupData, parent)
