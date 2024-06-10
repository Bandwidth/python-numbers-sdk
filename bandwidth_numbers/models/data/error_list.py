#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.error import Error
from bandwidth_numbers.models.maps.error_list import ErrorListMap

class ErrorList(ErrorListMap, BaseData):

    def __init__(self):
        self.error = BaseResourceList(Error)
