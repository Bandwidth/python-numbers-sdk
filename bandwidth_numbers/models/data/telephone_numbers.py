#!/usr/bin/env python

from bandwidth_numbers.models.data.telephone_number_detail_list_tn import \
    TelephoneNumberDetailListTn
from bandwidth_numbers.models.maps.telephone_numbers import TelephoneNumbersMap

class TelephoneNumbers(TelephoneNumbersMap, TelephoneNumberDetailListTn):

    def __init__(self, parent=None):
        TelephoneNumberDetailListTn.__init__(self, parent)
