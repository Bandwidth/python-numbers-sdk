#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList, \
    BaseResourceSimpleList
from bandwidth_numbers.models.data.file_data import FileData
from bandwidth_numbers.models.maps.loas import LoasMap

class LoasData(LoasMap, BaseData):

    def __init__(self):
        self.file_data = BaseResourceList(FileData)
        self.file_names = BaseResourceSimpleList()
