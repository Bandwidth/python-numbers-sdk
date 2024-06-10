#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.tn_line_options import TnLineOptionsData

XPATH_TN_LINE_OPTIONS = "/{}"

class TnLineOptions(BaseResource, TnLineOptionsData):

    _xpath = XPATH_TN_LINE_OPTIONS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TnLineOptionsData.__init__(self)
