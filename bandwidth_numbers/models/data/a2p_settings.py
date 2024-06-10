#!/usr/bin/env python
  
from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.a2p_settings import A2pSettingsMap

class A2pSettings(A2pSettingsMap, BaseData):
    pass
