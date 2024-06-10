#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.dlda_order_response import DldaOrderResponseMap

class DldaOrderResponseData(DldaOrderResponseMap, BaseData):
    pass
