#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from unittest import main, TestCase

import requests_mock

from bandwidth_numbers.client import Client
from bandwidth_numbers.models.account import Account

XML_RESPONSE_ACCOUNT_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b" <AccountResponse>"
    b"    <Account>"
    b"        <AccountId>123456</AccountId>"
    b"        <CompanyName>Spam</CompanyName>"
    b"        <AccountType>Ham</AccountType>"
    b"        <Tiers>"
    b"            <Tier>0</Tier>"
    b"        </Tiers>"
    b"        <Address>"
    b"            <HouseNumber>900</HouseNumber>"
    b"        </Address>"
    b"        <Contact>"
    b"            <FirstName>Eggs</FirstName>"
    b"        </Contact>"
    b"    </Account>"
    b"</AccountResponse>"
)

class ClassOAuthTest(TestCase):

    """Test Client OAuth handling"""

    @classmethod
    def setUpClass(cls):
        cls._valid_token_client = Client("http://foo", "bar", "bar", "qux", None, None, None, "access_token_1234")
        cls._valid_token_account = Account(client=cls._valid_token_client)

    @classmethod
    def tearDownClass(cls):
        del cls._valid_token_client
        del cls._valid_token_account

    def test_account_get(self):

        with requests_mock.Mocker() as m:

            url = self._valid_token_account.client.config.url + self._valid_token_account.get_xpath()
            expected_headers = {"Authorization": "Bearer access_token_1234"}
            m.get(url, content=XML_RESPONSE_ACCOUNT_GET, request_headers=expected_headers)

            self._valid_token_account.get()

            self.assertEqual(self._valid_token_account.id, "123456")
            self.assertEqual(self._valid_token_account.company_name, "Spam")
            self.assertEqual(self._valid_token_account.account_type, "Ham")
            self.assertEqual(self._valid_token_account.tiers.tier.items, ["0"])
            self.assertEqual(self._valid_token_account.address.house_number, "900")
            self.assertEqual(self._valid_token_account.contact.first_name, "Eggs")

if __name__ == "__main__":
    main()
