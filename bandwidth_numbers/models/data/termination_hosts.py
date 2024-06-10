#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.host import Host
from bandwidth_numbers.models.maps.termination_hosts import TerminationHostsMap

class TerminationHosts(TerminationHostsMap, BaseData):

    @property
    def items(self):
        return self.termination_host.items

    def __init__(self):
        self.termination_host = BaseResourceList(Host)

    def add(self):
        return self.termination_host.add()
