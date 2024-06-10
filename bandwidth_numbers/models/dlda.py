#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.dlda import DldaData
from bandwidth_numbers.models.dlda_order_response import DldaOrderResponse
from bandwidth_numbers.models.history import History

XML_NAME_DLDA = "DldaOrder"
XPATH_DLDA = "/{}"

class Dlda(BaseResource, DldaData):

    """ DLDA order """

    _node_name = XML_NAME_DLDA
    _xpath = XPATH_DLDA

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    @property
    def history(self):
        return self._history

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        DldaData.__init__(self)
        self._history = History(self, client)

    def get(self, id=None, params=None):
        return self._get_data(id)

    def save(self):
        str = self._save(True)
        self.clear()
        self._from_xml(self._element_from_string(str))
        return True
