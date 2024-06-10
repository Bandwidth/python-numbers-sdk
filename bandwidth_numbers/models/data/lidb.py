#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.lidb import LidbMap
from bandwidth_numbers.models.data.lidb_tn_groups import LidbTnGroups
from bandwidth_numbers.models.data.error_list import ErrorList

class LidbData(LidbMap, BaseData):

    @property
    def count_of_tns(self):
        return self.count_of_t_ns
    @count_of_tns.setter
    def count_of_tns(self, count_of_tns):
        self.count_of_t_ns = count_of_tns

    def __init__(self):
        self.lidb_tn_groups = LidbTnGroups()
        self.error_list = ErrorList()
