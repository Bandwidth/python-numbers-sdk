#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.permissions_list import PermissionsList
from bandwidth_numbers.models.maps.role import RoleMap

class Role(RoleMap, BaseData):

    @property
    def name(self):
        return self.role_name
    @name.setter
    def name(self, name):
        self.role_name = name

    def __init__(self):
        self.permissions = PermissionsList()
