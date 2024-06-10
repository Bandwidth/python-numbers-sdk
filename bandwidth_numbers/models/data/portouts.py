#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.links import Links
from bandwidth_numbers.models.maps.portins import PortInsMap
from bandwidth_numbers.models.portout import PortOut

class PortOutsData(PortInsMap, BaseData):

    def __init__(self, parent=None):
        self.links = Links()
        self.lnp_port_info_for_given_status = BaseResourceList(PortOut, parent)
