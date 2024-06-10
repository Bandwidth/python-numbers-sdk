#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.address import Address
from bandwidth_numbers.models.maps.subscriber import SubscriberMap

class Subscriber(SubscriberMap, BaseData):

    def __init__(self):
        self.service_address = Address()
