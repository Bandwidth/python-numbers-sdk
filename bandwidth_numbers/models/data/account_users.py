#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.data.account_user import AccountUser
from bandwidth_numbers.models.maps.account_users import AccountUsersMap

class AccountUsersData(AccountUsersMap, BaseData):

    def __init__(self):
        self.user = BaseResourceList(AccountUser)
