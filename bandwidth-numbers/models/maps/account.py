#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class AccountMap(BaseMap):

    account_id = None
    account_type = None
    address = None
    alt_spid = None
    company_name = None
    contact = None
    customer_name = None
    description = None
    is_new_sms_account = None
    lnp_enabled = None
    nena_id = None
    port_carrier_type = None
    reservation_allowed = None
    spid = None
    tiers = None