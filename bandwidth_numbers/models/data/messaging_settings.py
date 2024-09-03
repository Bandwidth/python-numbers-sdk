#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.messaging_settings import MessagingSettingsMap


class MessagingSettingsData(MessagingSettingsMap, BaseData):
    pass
