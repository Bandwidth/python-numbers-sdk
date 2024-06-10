#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.tn_status import TnStatus
from bandwidth_numbers.models.maps.tn_history import TnHistoryMap

class TnHistoryData(TnHistoryMap):

    def __init__(self):
        self.telephone_number_status = BaseResourceList(TnStatus)
