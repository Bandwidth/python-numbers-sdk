#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.ord.state_search_order import \
    StateSearchOrderMap

class StateSearchOrder(StateSearchOrderMap, BaseData):
    pass
