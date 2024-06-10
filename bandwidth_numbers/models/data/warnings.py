#!/usr/bin/env python
  
from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.warning import WarningCls
from bandwidth_numbers.models.maps.warnings import WarningsMap

class Warnings(WarningsMap, BaseData):

    def __init__(self):
        self.warning = BaseResourceList(WarningCls)
