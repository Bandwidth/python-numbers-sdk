#!/usr/bin/env python

from bandwidth_numbers.models.maps.base_map import BaseMap

class MessagingSettingsMap(BaseMap):
    sms_enabled = None
    campaign_id = None
    message_class = None
    campaign_fully_provisioned = None
    a2p_state = None
