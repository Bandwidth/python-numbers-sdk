#!/usr/bin/env python
  
from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.warning import WarningMap

class WarningCls(WarningMap, BaseData): #Warning is a reserved word in python
    pass
