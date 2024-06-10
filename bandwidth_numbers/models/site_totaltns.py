#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.site_totaltns import SiteTotaltnsData

XML_NAME_TOTALTNS_SITE = "SiteTNs"
XPATH_TOTALTNS_SITE = "/totaltns"

class SiteTotaltns(BaseResource, SiteTotaltnsData):

    """Total telephone numbers count for a site"""

    _node_name = XML_NAME_TOTALTNS_SITE
    _xpath = XPATH_TOTALTNS_SITE

    def get(self):
        return self._get_data()
