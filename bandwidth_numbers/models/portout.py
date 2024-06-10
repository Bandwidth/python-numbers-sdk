#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.portin import PortInData
from bandwidth_numbers.models.notes import Notes
from bandwidth_numbers.models.totals import Totals

XML_NAME_PORTOUT = "LnpOrderResponse"
XPATH_PORTOUT = "/{}"

class PortOut(BaseResource, PortInData):

    """Local number portability order from a winning carrier"""

    _node_name = XML_NAME_PORTOUT
    _xpath = XPATH_PORTOUT

    @property
    def notes(self):
        return self._notes

    @property
    def totals(self):
        return self._totals

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortInData.__init__(self)
        self._notes = Notes(self)
        self._totals = Totals(self, client)
