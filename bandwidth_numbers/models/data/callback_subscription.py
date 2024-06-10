#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.callback_subscription import CallbackSubscriptionMap

class CallbackSubscription(CallbackSubscriptionMap, BaseData):
    pass
