#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.contact import ContactMap

class Contact(ContactMap, BaseData):
    pass
