#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class ErrorMap(BaseMap):

    code = None
    description = None
    error_code = None
    telephone_number = None