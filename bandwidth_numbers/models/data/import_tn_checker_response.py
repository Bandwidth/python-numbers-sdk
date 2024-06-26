#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.import_tn_checker_payload import ImportTnCheckerResponse
from bandwidth_numbers.models.maps.import_tn_checker_response import ImportTnCheckerResponseMap

class ImportTnCheckerResponseData(ImportTnCheckerResponseMap, BaseData):

    def __init__(self):
        self.import_tn_checker_payload = ImportTnCheckerResponse()
