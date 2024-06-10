#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.available_npa_nxx import AvailableNpaNxxData

XML_NAME_AVAILABLE_NPA_NXX = "SearchResultForAvailableNpaNxx"
XPATH_AVAILABLE_NPA_NXX = "/availableNpaNxx"

class AvailableNpaNxx(BaseResource, AvailableNpaNxxData):

    """Available NPA/NXX for account"""

    _node_name = XML_NAME_AVAILABLE_NPA_NXX
    _xpath = XPATH_AVAILABLE_NPA_NXX

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        AvailableNpaNxxData.__init__(self)

    def list(self, params):
        return self.get(params=params).available_npa_nxx_list.\
            available_npa_nxx
