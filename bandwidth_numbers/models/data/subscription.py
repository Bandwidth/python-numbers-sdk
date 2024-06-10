#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.email_subscription import EmailSubscription
from bandwidth_numbers.models.data.callback_subscription import CallbackSubscription
from bandwidth_numbers.models.maps.subscription import SubscriptionMap

class SubscriptionData(SubscriptionMap, BaseData):

    def __init__(self):
        self.email_subscription = EmailSubscription()
        self.callback_subscription = CallbackSubscription()
