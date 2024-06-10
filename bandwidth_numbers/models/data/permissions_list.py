#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.permission import Permission
from bandwidth_numbers.models.maps.permissions_list import PermissionsListMap

class PermissionsList(PermissionsListMap, BaseData):

    @property
    def items(self):
        return self.permission.items

    def __init__(self):
        self.permission = BaseResourceList(Permission)
