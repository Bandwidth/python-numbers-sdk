#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.error import ErrorMap

class Error(ErrorMap, BaseData):
    pass
