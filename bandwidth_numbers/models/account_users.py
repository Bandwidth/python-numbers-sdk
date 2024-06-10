#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.account_users import AccountUsersData

XML_NAME_USERS_ACC = "Users"
XPATH_USERS_ACC = "/users"

class AccountUsers(BaseResource, AccountUsersData):

    """Account users details"""

    _node_name = XML_NAME_USERS_ACC
    _xpath = XPATH_USERS_ACC

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        AccountUsersData.__init__(self)

    def list(self):
        return self._get_data().user
