#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.site_host import SiteHost
from bandwidth_numbers.models.maps.site_hosts import SiteHostsMap

class SiteHostsData(SiteHostsMap, BaseData):

    @property
    def items(self):
        return self.site_host.items

    def __init__(self):
        self.site_host = BaseResourceList(SiteHost)
