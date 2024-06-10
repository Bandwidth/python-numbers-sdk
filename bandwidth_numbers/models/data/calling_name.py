#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.calling_name import CallingNameMap

class CallingName(CallingNameMap, BaseData):
    pass
