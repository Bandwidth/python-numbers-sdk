#!/usr/bin/env python

from bandwidth_numbers.models.maps.base_map import BaseMap

class OrderHistoryMap(BaseMap):

    order_date = None
    note = None
    author = None
    status = None
    difference = None
