#!/usr/bin/env python

from future import standard_library

import os
import time

from bandwidth_numbers.utils.py_compat import PY_VER_MAJOR

if PY_VER_MAJOR < 3:
    from io import open

from configparser import ConfigParser

MAX_FILE_SIZE = 1048576
SECTION_ACCOUNT = "account"
SECTION_SRV = "rest"
VALUE_ACCOUNT_ID = "account_id"
VALUE_PASSWORD = "password"
VALUE_URL = "url"
VALUE_USERNAME = "username"
VALUE_CLIENT_ID = "client_id"
VALUE_CLIENT_SECRET = "client_secret"
VALUE_ACCESS_TOKEN = "access_token"
VALUE_ACCESS_TOKEN_EXPIRATION = "access_token_expiration"

class ConfigData(object):

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def client_id(self):
        return self._client_id
    
    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id

    @property
    def client_secret(self):
        return self._client_secret
    
    @client_secret.setter
    def client_secret(self, client_secret):
        self._client_secret = client_secret

    @property
    def access_token(self):
        return self._access_token
    
    @access_token.setter
    def access_token(self, access_token):
        self._access_token = access_token

    @property
    def access_token_expiration(self):
        return self._access_token_expiration
    
    @access_token_expiration.setter
    def access_token_expiration(self, access_token_expiration):
        self._access_token_expiration = access_token_expiration

class Config(ConfigData):

    """Connection and auth settings"""

    def __init__(
            self, url=None, account_id=None, username=None, password=None,
            filename=None, client_id=None, client_secret=None,
            access_token=None, access_token_expiration=int(time.time()) + 3600):

        if filename is None:
            self._account_id = account_id
            self._username = username
            self._password = password
            self._url = url
            self._client_id = client_id
            self._client_secret = client_secret
            self._access_token = access_token
            self._access_token_expiration = access_token_expiration
        else:
            self._account_id = None
            self._username = None
            self._password = None
            self._url = None
            self._client_id = None
            self._client_secret = None
            self._access_token = None
            self._access_token_expiration = int(time.time()) + 3600
            self.load_from_file(filename)

    def load_from_file(self, filename=None):

        """
        Loads config values from "filename".

        See the default file for structure.
        Configs larger than MAX_FILE_SIZE are skipped.
        Leading and trailing whitespace is removed.

        Args:
            filename: a UTF-8 config file.
        """

        # Skip non-existing and huge files

        if not os.path.isfile(filename):
            raise ValueError("Config file doesn't exist")

        if os.path.getsize(filename) > MAX_FILE_SIZE:
            raise ValueError("Config too large")

        with open(filename, encoding="UTF-8") as fp:
            self._parser = ConfigParser(allow_no_value = True)
            if PY_VER_MAJOR == 3:
                self._parser.read_file(fp)
            else:
                self._parser.readfp(fp)

        self._account_id = self._parser.get(
            SECTION_ACCOUNT, VALUE_ACCOUNT_ID
        )
        self._account_id = self._account_id.strip()

        self._username = self._parser.get(SECTION_ACCOUNT, VALUE_USERNAME, fallback=None)
        self._username = self._username.strip() if self._username else None

        self._password = self._parser.get(SECTION_ACCOUNT, VALUE_PASSWORD, fallback=None)
        self._password = self._password.strip() if self._password else None

        self._url = self._parser.get(SECTION_SRV, VALUE_URL, fallback=None)
        self._url = self._url.strip() if self._url else None

        self._client_id = self._parser.get(SECTION_ACCOUNT, VALUE_CLIENT_ID, fallback=None)
        self._client_id = self._client_id.strip() if self._client_id else None

        self._client_secret = self._parser.get(SECTION_ACCOUNT, VALUE_CLIENT_SECRET, fallback=None)
        self._client_secret = self._client_secret.strip() if self._client_secret else None

        self._access_token = self._parser.get(SECTION_ACCOUNT, VALUE_ACCESS_TOKEN, fallback=None)
        self._access_token = self._access_token.strip() if self._access_token else None

        self._access_token_expiration = self._parser.get(SECTION_ACCOUNT,
                                                         VALUE_ACCESS_TOKEN_EXPIRATION,
                                                         fallback=int(time.time()) + 3600)
