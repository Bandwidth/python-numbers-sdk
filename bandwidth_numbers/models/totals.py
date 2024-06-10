#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.totals import TotalsData

XML_NAME_TOTALS = "Quantity"
XPATH_TOTALS = "/totals"

class Totals(BaseResource, TotalsData):

    """Telephone numbers totals for resource"""

    _node_name = XML_NAME_TOTALS
    _xpath = XPATH_TOTALS

    def get(self):
        return self._get_data()
