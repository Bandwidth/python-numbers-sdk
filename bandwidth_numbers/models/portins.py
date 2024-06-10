#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.portins import PortInsData
from bandwidth_numbers.models.portin import PortIn

XML_NAME_PORTINS = "LNPResponseWrapper"
XPATH_PORTINS = "/portins"

class PortIns(BaseResource, PortInsData):

    """Local number portability orders for account"""

    _node_name = XML_NAME_PORTINS
    _xpath = XPATH_PORTINS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortInsData.__init__(self, self)

    def create(self, data=None, save=True):
        portin = PortIn(self).set_from_dict(data)
        if save and (data is not None):
            portin.save()
        return portin

    def get(self, id, params):
        return PortIn(self).get(id, params=params)

    def list(self, params):
        return self._get_data(params=params).lnp_port_info_for_given_status
