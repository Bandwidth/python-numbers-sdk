#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.city import CityMap

class City(CityMap, BaseData):

    @property
    def city(self):
        return self.name
    @city.setter
    def city(self, city):
        self.name = city
