#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.losing_carrier_tn_list import LosingCarrierTnList
from bandwidth_numbers.models.maps.lnp_losing_carriers import LnpLosingCarriersMap

class LnpLosingCarriers(LnpLosingCarriersMap, BaseData):

    def __init__(self):
        self.losing_carrier_tn_list = LosingCarrierTnList()
