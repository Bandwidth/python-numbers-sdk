#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.role import Role
from bandwidth_numbers.models.maps.roles_list import RolesListMap

class RolesList(RolesListMap, BaseData):

    @property
    def items(self):
        return self.role.items

    def __init__(self):
        self.role = BaseResourceList(Role)
