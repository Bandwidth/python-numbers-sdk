#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.dlda_tn_groups import DldaTnGroupsMap
from bandwidth_numbers.models.data.dlda_tn_group import DldaTnGroupData

class DldaTnGroups(DldaTnGroupsMap, BaseData):

    def __init__(self):
        self.dlda_tn_group = BaseResourceList(DldaTnGroupData)
