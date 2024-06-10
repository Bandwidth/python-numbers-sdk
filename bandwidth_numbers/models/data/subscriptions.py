#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.maps.subscriptions import SubscriptionsMap
from bandwidth_numbers.models.subscription import Subscription

class SubscriptionsData(SubscriptionsMap, BaseData):

    def __init__(self, parent=None):
        self.subscription = BaseResourceList(Subscription, parent)
