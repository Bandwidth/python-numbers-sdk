#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.tn_status import TnStatusMap

class TnStatus(TnStatusMap, BaseData):
    pass
