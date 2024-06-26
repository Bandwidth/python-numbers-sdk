#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.data.error_list import ErrorList
from bandwidth_numbers.models.data.ord.area_code_search_order import \
    AreaCodeSearchOrder
from bandwidth_numbers.models.data.ord.city_search_order import \
    CitySearchOrder
from bandwidth_numbers.models.data.ord.existing_search_order import \
    ExistingSearchOrder
from bandwidth_numbers.models.data.ord.lata_search_order import \
    LataSearchOrder
from bandwidth_numbers.models.data.ord.npa_search_order import \
    NpaSearchOrder
from bandwidth_numbers.models.data.ord.rate_center_search_order import \
    RateCenterSearchOrder
from bandwidth_numbers.models.data.ord.state_search_order import \
    StateSearchOrder
from bandwidth_numbers.models.data.ord.vanity_search_order import \
    VanitySearchOrder
from bandwidth_numbers.models.data.ord.wildcard_search_order import \
    WildcardSearchOrder
from bandwidth_numbers.models.data.ord.zip_search_order import \
    ZipSearchOrder
from bandwidth_numbers.models.data.telephone_number_list import TelephoneNumberList
from bandwidth_numbers.models.maps.order import OrderMap

class OrderData(OrderMap, BaseData):

    @property
    def count_of_tns(self):
        return self.count_of_t_ns
    @count_of_tns.setter
    def count_of_tns(self, count_of_tns):
        self.count_of_t_ns = count_of_tns

    def __init__(self):
        self.area_code_search_and_order_type = AreaCodeSearchOrder()
        self.city_search_and_order_type = CitySearchOrder()
        self.existing_telephone_number_order_type = ExistingSearchOrder()
        self.lata_search_and_order_type = LataSearchOrder()
        self.npanxx_search_and_order_type = NpaSearchOrder()
        self.rate_center_search_and_order_type = RateCenterSearchOrder()
        self.state_search_and_order_type = StateSearchOrder()
        self.telephone_number_list = TelephoneNumberList()
        self.toll_free_vanity_search_and_order_type = VanitySearchOrder()
        self.toll_free_wild_char_search_and_order_type = WildcardSearchOrder()
        self.zip_search_and_order_type = ZipSearchOrder()

    def add_reservation(self, id):
        return self.existing_telephone_number_order_type.\
            reservation_id_list.add(id)

    def add_tn(self, number):
        return self.existing_telephone_number_order_type.\
            telephone_number_list.add(number)
