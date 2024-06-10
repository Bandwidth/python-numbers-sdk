#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.response_status import ResponseStatusMap

class ResponseStatus(ResponseStatusMap, BaseData):
    pass
