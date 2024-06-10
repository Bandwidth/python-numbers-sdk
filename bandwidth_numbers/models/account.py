#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.account_users import AccountUsers
from bandwidth_numbers.models.available_npa_nxx import AvailableNpaNxx
from bandwidth_numbers.models.available_numbers import AvailableNumbers
from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.account import AccountData
from bandwidth_numbers.models.disc_numbers import DiscNumbers
from bandwidth_numbers.models.disconnects import Disconnects
from bandwidth_numbers.models.in_service_numbers import InServiceNumbers
from bandwidth_numbers.models.line_option_orders import LineOptionOrder
from bandwidth_numbers.models.import_tn_checker import ImportTnChecker
from bandwidth_numbers.models.lnpchecker import LnpChecker
from bandwidth_numbers.models.orders import Orders
from bandwidth_numbers.models.lidbs import Lidbs
from bandwidth_numbers.models.dldas import Dldas
from bandwidth_numbers.models.subscriptions import Subscriptions
from bandwidth_numbers.models.portins import PortIns
from bandwidth_numbers.models.portouts import PortOuts
from bandwidth_numbers.models.reservation import Reservation
from bandwidth_numbers.models.site_hosts import SiteHosts
from bandwidth_numbers.models.sites import Sites
from bandwidth_numbers.models.tn_option_orders import TnOptionOrders

XPATH_ACCOUNT = "/accounts/{}"

class Account(BaseResource, AccountData):

    """Iris account"""

    _xpath = XPATH_ACCOUNT

    @property
    def available_npa_nxx(self):
        return self._available_npa_nxx

    @property
    def available_numbers(self):
        return self._available_numbers

    @property
    def disconnected_numbers(self):
        return self._disconnected_numbers

    @property
    def disconnects(self):
        return self._disconnects

    @property
    def dldas(self):
        return self._dldas

    @property
    def hosts(self):
        return self._hosts

    @property
    def id(self):
        return self.account_id
    @id.setter
    def id(self, id):
        self.account_id = id

    @property
    def import_tn_checker(self):
        return self._import_tn_checker

    @property
    def in_service_numbers(self):
        return self._in_service_numbers

    @property
    def lidbs(self):
        return self._lidbs

    @property
    def line_option_orders(self):
        return self._line_option_orders

    @property
    def lnpchecker(self):
        return self._lnpchecker

    @property
    def orders(self):
        return self._orders

    @property
    def portins(self):
        return self._portins

    @property
    def portouts(self):
        return self._portouts

    @property
    def sites(self):
        return self._sites

    @property
    def subscriptions(self):
        return self._subscriptions

    @property
    def tnreservation(self):
        return self._tnreservation

    @property
    def users(self):
        return self._users

    @property
    def tn_option_orders(self):
        return self._tn_option_orders

    def __init__(self, parent=None, client=None):
        if client is not None:
            self.id = client.config.account_id
        super().__init__(parent, client)
        AccountData.__init__(self)
        self._available_npa_nxx = AvailableNpaNxx(self, client)
        self._available_numbers = AvailableNumbers(self, client)
        self._disconnected_numbers = DiscNumbers(self, client)
        self._disconnects = Disconnects(self, client)
        self._hosts = SiteHosts(self, client)
        self._import_tn_checker = ImportTnChecker(self, client)
        self._in_service_numbers = InServiceNumbers(self, client)
        self._line_option_orders = LineOptionOrder(self, client)
        self._lnpchecker = LnpChecker(self, client)
        self._orders = Orders(self, client)
        self._portins = PortIns(self, client)
        self._portouts = PortOuts(self, client)
        self._lidbs = Lidbs(self, client)
        self._dldas = Dldas(self, client)
        self._subscriptions = Subscriptions(self, client)
        self._sites = Sites(self, client)
        self._tnreservation = Reservation(self, client)
        self._users = AccountUsers(self, client)
        self._tn_option_orders = TnOptionOrders(self, client)

    def get(self, id=None):
        return self._get_data(id)
