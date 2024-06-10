#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.email_subscription import EmailSubscriptionMap

class EmailSubscription(EmailSubscriptionMap, BaseData):
    pass
