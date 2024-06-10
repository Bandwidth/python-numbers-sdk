#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.lidbs import LidbsMap
from bandwidth_numbers.models.lidb import Lidb

class LidbsData(LidbsMap, BaseData):

    def __init__(self, parent=None):
        self.order_id_user_id_date = BaseResourceList(Lidb, parent)
