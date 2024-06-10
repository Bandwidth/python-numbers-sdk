#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.maps.file_meta_data import FileMetaDataMap

XPATH_METADATA = "/{}/metadata"

class FileMetaData(BaseResource, FileMetaDataMap):

    """LOAs metadata"""

    _xpath = XPATH_METADATA
    _xpath_save = _xpath

    def get(self, id):
        return self._get_data(id)
