#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseResourceSimpleList
from bandwidth_numbers.models.data.location import Location
from bandwidth_numbers.models.data.npanxx_list import NpanxxList
from bandwidth_numbers.models.maps.tn_lca import TnLcaMap

class TnLcaData(TnLcaMap):

    def __init__(self):
        self.listof_npanxx = NpanxxList()
        self.location = Location()
