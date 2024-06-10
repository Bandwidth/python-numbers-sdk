#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.city import City
from bandwidth_numbers.models.maps.cities_list import CitiesListMap

class CitiesList(CitiesListMap, BaseData):

    def __init__(self):
        self.city = BaseResourceList(City)
