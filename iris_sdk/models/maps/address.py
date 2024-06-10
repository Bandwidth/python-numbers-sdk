#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class AddressMap(BaseMap):

    address_line2 = None
    address_type = None
    city = None
    county = None
    country = None
    house_number = None
    house_prefix = None
    house_suffix = None
    plus_four = None
    pre_directional = None
    post_directional = None
    state_code = None
    street_name = None
    street_suffix = None
    zip = None