#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.cities_list import CitiesList
from bandwidth_numbers.models.maps.cities import CitiesMap

class CitiesData(CitiesMap, BaseData):

    def __init__(self):
        self.cities = CitiesList()
