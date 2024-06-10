#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.host import HostMap

class Host(HostMap, BaseData):
    pass
