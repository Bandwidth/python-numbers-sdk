#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.activation_status import ActivationStatusData

XPATH_ACTIVATION_STATUS = "/activationStatus"

class ActivationStatus(BaseResource, ActivationStatusData):

    """Local number portability order activation status"""

    _xpath = XPATH_ACTIVATION_STATUS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        ActivationStatusData.__init__(self)
        self._id = 1

    def get(self):
        return self._get_data()

    def save(self):
        self.id = 1
        self._save()
