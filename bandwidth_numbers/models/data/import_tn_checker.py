#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.import_tn_checker_list import TelephoneNumbers
from bandwidth_numbers.models.maps.import_tn_checker import ImportTnCheckerMap

class ImportTnCheckerData(ImportTnCheckerMap, BaseData):

    def __init__(self):
        self.telephone_numbers = TelephoneNumbers()
