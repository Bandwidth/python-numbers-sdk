#!/usr/bin/env python

from __future__ import division, absolute_import, print_function

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.messaging_settings import MessagingSettingsData

XML_NAME_MESSAGING_SETTINGS = "MessagingSettings"

class MessagingSettings(BaseResource, MessagingSettingsData):
    pass
