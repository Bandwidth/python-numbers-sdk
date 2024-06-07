#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.lidbs import LidbsMap
from iris_sdk.models.lidb import Lidb

class LidbsData(LidbsMap, BaseData):

    def __init__(self, parent=None):
        self.order_id_user_id_date = BaseResourceList(Lidb, parent)