#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.roles_list import RolesList
from bandwidth_numbers.models.maps.account_user import AccountUserMap

class AccountUser(AccountUserMap, BaseData):

    def __init__(self):
        self.roles = RolesList()
