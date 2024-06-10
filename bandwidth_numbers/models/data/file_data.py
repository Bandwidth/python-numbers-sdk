#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.file_meta_data import FileMetaDataData
from bandwidth_numbers.models.maps.file_data import FileDataMap

class FileData(FileDataMap, BaseData):

    def __init__(self):
        self.file_meta_data = FileMetaDataData()
