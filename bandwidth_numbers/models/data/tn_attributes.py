#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.tn_attributes import TnAttributesMap

class TnAttributes(TnAttributesMap, BaseData):

    @property
    def items(self):
        return self.tn_attribute.items

    def __init__(self, parent=None):
        self.tn_attribute = BaseResourceSimpleList()
