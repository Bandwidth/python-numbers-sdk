#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.sites import SitesMap
from bandwidth_numbers.models.site import Site

class SitesData(SitesMap, BaseData):

    def __init__(self, parent=None):
        self.site = BaseResourceList(Site, self)
