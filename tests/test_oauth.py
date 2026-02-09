#!/usr/bin/env python

import os
import sys
import time

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
    b"    </Account>"
    b"</AccountResponse>"
)

class ClassOAuthTest(TestCase):

    """Test Client OAuth handling"""

    @classmethod
    def setUpClass(cls):
        url = "https://api.com"
        account_id = "account_id_1234"
        username = "username"
        password = "password"
        client_id = "client_id_1234"
        client_secret = "client_secret_5678"
        access_token = "access_token_1234"
        access_token_expiration = int(time.time()) + 3600
        cls._basic_auth_client = Client(url, account_id, username, password)
        cls._basic_auth_account = Account(client=cls._basic_auth_client)
        cls._valid_token_client = Client(url, account_id, username, password, None, None, None, access_token, access_token_expiration)
        cls._valid_token_account = Account(client=cls._valid_token_client)
        cls._client_credentials_client = Client(url, account_id, username, password, None, client_id, client_secret)
        cls._client_credentials_account = Account(client=cls._client_credentials_client)
        cls._expired_token_client = Client(url, account_id, username, password, None, client_id, client_secret, access_token, int(time.time()) - 3600)
        cls._expired_token_account = Account(client=cls._expired_token_client)

    @classmethod
    def tearDownClass(cls):
        del cls._basic_auth_client
        del cls._basic_auth_account
        del cls._valid_token_client
        del cls._valid_token_account
        del cls._client_credentials_client
        del cls._client_credentials_account
        del cls._expired_token_client
        del cls._expired_token_account

    def test_basic_auth(self):
        
        with requests_mock.Mocker() as m:
            url = self._basic_auth_account.client.config.url + self._basic_auth_account.get_xpath()
            expected_headers = {"Authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ="}
            m.get(url, content=XML_RESPONSE_ACCOUNT_GET, request_headers=expected_headers)

            self._basic_auth_account.get()
            self.assertEqual(self._basic_auth_account.id, "123456")

    def test_valid_token(self):

        with requests_mock.Mocker() as m:
            url = self._valid_token_account.client.config.url + self._valid_token_account.get_xpath()
            expected_headers = {"Authorization": "Bearer access_token_1234"}
            m.get(url, content=XML_RESPONSE_ACCOUNT_GET, request_headers=expected_headers)

            self._valid_token_account.get()
            self.assertEqual(self._valid_token_account.id, "123456")

    def test_client_credentials(self):

        with requests_mock.Mocker() as m:
            token_url = 'https://api.bandwidth.com/api/v1/oauth2/token'
            m.post(token_url, json={
                'access_token': 'new_access_token_5678',
                'expires_in': 3600
            })

            url = self._client_credentials_account.client.config.url + self._client_credentials_account.get_xpath()
            expected_headers = {"Authorization": "Bearer new_access_token_5678"}
            m.get(url, content=XML_RESPONSE_ACCOUNT_GET, request_headers=expected_headers)

            self._client_credentials_account.get()
            self.assertEqual(self._client_credentials_account.id, "123456")

    def test_expired_token(self):

        with requests_mock.Mocker() as m:
            token_url = 'https://api.bandwidth.com/api/v1/oauth2/token'
            m.post(token_url, json={
                'access_token': 'new_access_token_1234',
                'expires_in': 3600
            })

            url = self._expired_token_account.client.config.url + self._expired_token_account.get_xpath()
            expected_headers = {"Authorization": "Bearer new_access_token_1234"}
            m.get(url, content=XML_RESPONSE_ACCOUNT_GET, request_headers=expected_headers)

            self._expired_token_account.get()
            self.assertEqual(self._expired_token_account.id, "123456")

if __name__ == "__main__":
    main()
