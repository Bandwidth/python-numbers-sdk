#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceSimpleList
from bandwidth_numbers.models.maps.cities_short_list import CitiesShortListMap

class CitiesShortList(CitiesShortListMap, BaseData):

    @property
    def items(self):
        return self.city.items

    def __init__(self):
        self.city = BaseResourceSimpleList()
