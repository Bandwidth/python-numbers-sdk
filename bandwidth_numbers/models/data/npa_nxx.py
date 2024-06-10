#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.npa_nxx import NpaNxxMap

class NpaNxx(NpaNxxMap, BaseData):
    pass
