#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.address import AddressMap

class Address(AddressMap, BaseData):
    pass
