#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.wireless_info import WirelessInfoMap

class WirelessInfo(WirelessInfoMap, BaseData):
    pass
