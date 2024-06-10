#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.features import Features
from bandwidth_numbers.models.maps.tndetails import TndetailsMap

class TndetailsData(TndetailsMap, BaseData):

    @property
    def id(self):
        return self.full_number
    @id.setter
    def id(self, id):
        self.full_number = id

    @property
    def last_modified_date(self):
        return self.last_modified
    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        self.last_modified = last_modified_date

    def __init__(self):
        self.features = Features()
