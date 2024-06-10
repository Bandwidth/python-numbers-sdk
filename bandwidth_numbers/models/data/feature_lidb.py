#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.feature_lidb import FeatureLidbMap

class FeatureLidb(FeatureLidbMap, BaseData):
    pass
