#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.file_meta_data import FileMetaDataMap

class FileMetaDataData(FileMetaDataMap, BaseData):
    pass
