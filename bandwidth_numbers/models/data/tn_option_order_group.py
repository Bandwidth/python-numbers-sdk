#!/usr/bin/env python
  
from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.tn_option_order_group import TnOptionOrderGroupMap
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.data.a2p_settings import A2pSettings

class TnOptionOrderGroupData(TnOptionOrderGroupMap, BaseData):

    def __init__(self, parent=None):
        self.telephone_numbers = TelephoneNumberList()
        self.a2p_settings = A2pSettings()
