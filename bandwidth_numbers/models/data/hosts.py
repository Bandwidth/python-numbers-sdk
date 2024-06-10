#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.host import Host
from bandwidth_numbers.models.maps.hosts import HostsMap

class Hosts(HostsMap, BaseData):

    @property
    def items(self):
        return self.host.items

    def __init__(self):
        self.host = BaseResourceList(Host)

    def add(self):
        return self.host.add()
