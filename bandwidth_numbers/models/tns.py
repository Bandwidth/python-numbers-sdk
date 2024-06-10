#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource, BaseResourceList
from bandwidth_numbers.models.data.tns import TnsData
from bandwidth_numbers.models.data.telephone_numbers import TelephoneNumbers
from bandwidth_numbers.models.telephone_number import TelephoneNumber

XML_NAME_TNS = "TelephoneNumbersResponse"
XPATH_TNS = "/tns"

class Tns(BaseResource, TnsData):

    """Telephone numbers directory"""

    _node_name = XML_NAME_TNS
    _xpath = XPATH_TNS

    @property
    def telephone_numbers(self):
        return self._telephone_numbers

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TnsData.__init__(self)
        self._telephone_numbers = TelephoneNumbers(self)

    def get(self, id):
        return TelephoneNumber(self).get(id)

    def list(self, params):
        self._get_data(params=params)
        return self.telephone_numbers.telephone_number
