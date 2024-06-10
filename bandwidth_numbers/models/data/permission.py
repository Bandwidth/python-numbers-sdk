#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.permission import PermissionMap

class Permission(PermissionMap, BaseData):

    @property
    def name(self):
        return self.permission_name
    @name.setter
    def name(self, name):
        self.permission_name = name
