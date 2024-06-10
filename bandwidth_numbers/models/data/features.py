#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.feature_dlda import FeatureDlda
from bandwidth_numbers.models.data.feature_lidb import FeatureLidb
from bandwidth_numbers.models.maps.features import FeaturesMap

class Features(FeaturesMap, BaseData):

    def __init__(self):
        self.dlda = FeatureDlda()
        self.lidb = FeatureLidb()
