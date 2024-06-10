#!/usr/bin/env python

from bandwidth_numbers.models.data.address import Address
from bandwidth_numbers.models.maps.site import SiteMap

class SiteData(SiteMap):

    def __init__(self):
        self.address = Address()
