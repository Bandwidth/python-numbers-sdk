#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.tn_rc_list import TelephoneNumberRcListMap

class TelephoneNumberRcList(TelephoneNumberRcListMap, BaseData):

    @property
    def items(self):
        return self.rc.items

    def __init__(self):
        self.rc = BaseResourceSimpleList()
