#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.lidb_tn_group import LidbTnGroupData
from bandwidth_numbers.models.maps.lidb_tn_groups import LidbTnGroupsMap

class LidbTnGroups(LidbTnGroupsMap, BaseData):

    def __init__(self):
        self.lidb_tn_group = BaseResourceList(LidbTnGroupData)
