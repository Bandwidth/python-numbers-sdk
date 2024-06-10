#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.dlda import DldaMap
from bandwidth_numbers.models.data.dlda_tn_groups import DldaTnGroups
from bandwidth_numbers.models.data.error_list import ErrorList

class DldaData(DldaMap, BaseData):

    @property
    def count_of_tns(self):
        return self.count_of_t_ns
    @count_of_tns.setter
    def count_of_tns(self, count_of_tns):
        self.count_of_t_ns = count_of_tns

    def __init__(self):
        self.dlda_tn_groups = DldaTnGroups()
        self.error_list = ErrorList()
