#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.zip_code_list import ZipCodeListMap

class ZipCodeList(ZipCodeListMap, BaseData):

    @property
    def items(self):
        return self.zip_code.items

    def __init__(self):
        self.zip_code = BaseResourceSimpleList()
