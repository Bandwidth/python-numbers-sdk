#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.address import Address
from bandwidth_numbers.models.data.contact import Contact
from bandwidth_numbers.models.data.tier_list import TierList
from bandwidth_numbers.models.maps.account import AccountMap

class AccountData(AccountMap, BaseData):

    def __init__(self):
        self.address = Address()
        self.contact = Contact()
        self.tiers = TierList()
