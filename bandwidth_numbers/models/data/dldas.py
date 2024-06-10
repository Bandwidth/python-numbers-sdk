#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.dldas import DldasMap
from bandwidth_numbers.models.dlda import Dlda

class DldasData(DldasMap, BaseData):

    def __init__(self, parent=None):
        self.order_id_user_id_date = BaseResourceList(Dlda, parent)
