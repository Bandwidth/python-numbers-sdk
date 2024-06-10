#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.lidb_tn_group import LidbTnGroupMap
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList

class LidbTnGroupData(LidbTnGroupMap, BaseData):

    def __init__(self):
        self.telephone_numbers = TelephoneNumberList()
