#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from bandwidth_numbers.utils.py_compat import PY_VER_MAJOR

from unittest import main, TestCase

if PY_VER_MAJOR == 3:
    from unittest.mock import patch, MagicMock, PropertyMock, ANY
else:
    from mock import patch, MagicMock, PropertyMock, ANY

from bandwidth_numbers.client import Client
from bandwidth_numbers.utils.bearer_auth import BearerAuth

class ClassClientInitTest(TestCase):

    """Test class initialization and properties."""

    @classmethod
    def setUpClass(cls):
        with patch("bandwidth_numbers.utils.config.Config"):
            cls._client = Client()

    @classmethod
    def tearDownClass(cls):
        del cls._client

    def test_client_config_prop(self):
        self._client._config = "foo"
        self.assertEqual(self._client._config, self._client.config)

class ClassClientConfigTest(TestCase):

    """Test class config."""

    def setUp(self):
        self._client = None

    def tearDown(self):
        del self._client

    @patch("bandwidth_numbers.utils.rest.RestClient.__init__", return_value = None)
    @patch("bandwidth_numbers.utils.config.Config.__init__", return_value = None)
    def test_client_init(self, mock1, mock2):
        self._client = Client("foo", "bar", "baz", "qux", "quux", "oof", "rab", "zab", 1337)
        mock1.assert_called_once_with("foo", "bar", "baz", "qux", "quux", "oof", "rab", "zab", 1337)
        mock2.assert_any_call()

class ClassClientStrings(TestCase):

    """Test string manipulation."""

    @classmethod
    def setUpClass(cls):
        with patch("bandwidth_numbers.utils.config.Config"):
            with patch("bandwidth_numbers.utils.rest.RestClient"):
                cls._client = Client("foo///")

    @classmethod
    def tearDownClass(cls):
        del cls._client

    def test_client_get_uri_no_section(self):
        str = self._client._get_uri()
        self.assertEqual(str, "foo")

    def test_client_get_uri_with_section(self):
        str = self._client._get_uri("///bar/baz///")
        self.assertEqual(str, "foo/bar/baz")

class ClassClientRequests(TestCase):

    """Test rest requests."""

    def setUp(self):

        patcher_req = patch("bandwidth_numbers.utils.rest.RestClient.request")
        patcher_url = patch("bandwidth_numbers.utils.config.Config.url",
            new_callable = PropertyMock, return_value = "foo")
        patcher_pass = patch("bandwidth_numbers.utils.config.Config.password",
            new_callable = PropertyMock, return_value = "bar")
        patcher_user = patch("bandwidth_numbers.utils.config.Config.username",
            new_callable = PropertyMock, return_value = "baz")
        patcher_token = patch("bandwidth_numbers.utils.config.Config.access_token",
            new_callable = PropertyMock, return_value = None)
        patcher_exp = patch("bandwidth_numbers.utils.config.Config.access_token_expiration",
            new_callable = PropertyMock, return_value = 0)
        patcher_client_id = patch("bandwidth_numbers.utils.config.Config.client_id",
            new_callable = PropertyMock, return_value = None)
        patcher_client_secret = patch("bandwidth_numbers.utils.config.Config.client_secret",
            new_callable = PropertyMock, return_value = None)

        self._url = patcher_url.start()
        self._pass = patcher_pass.start()
        self._request = patcher_req.start()
        self._user = patcher_user.start()
        self._token = patcher_token.start()
        self._exp = patcher_exp.start()
        self._client_id = patcher_client_id.start()
        self._client_secret = patcher_client_secret.start()

        self._request.return_value = self._mock_res

        self.addCleanup(patch.stopall)

    @classmethod
    def setUpClass(cls):

        cls._mock_res = MagicMock("requests.models.Request")
        cls._mock_res.headers = {"location": "return/return1"}
        cls._mock_res.content = b"foobar"
        cls._mock_res.status_code = 1337

        with patch("bandwidth_numbers.utils.config.Config"):
            with patch("bandwidth_numbers.utils.rest.RestClient"):
                cls._client = Client()

    @classmethod
    def tearDownClass(cls):
        del cls._client

    def test_client_delete(self):
        res = self._client.delete("qux")
        self._request.assert_called_once_with("DELETE",
            url="foo/qux",
            auth=(self._user.return_value, self._pass.return_value),
            params=None, data=None, headers=None)

    def test_client_get(self):
        res = self._client.get("", "qux")
        self._request.assert_called_once_with("GET",
            url=self._url.return_value,
            auth=(self._user.return_value, self._pass.return_value),
            params="qux", data=None, headers=None)

    def test_client_post(self):
        res = self._client.post("", "qux", "quux")
        self._request.assert_called_once_with("POST",
            url=self._url.return_value,
            auth=(self._user.return_value, self._pass.return_value),
            params="qux", data="quux", headers=None)

    def test_client_put(self):
        self._request.return_value.status_code = 200
        res = self._client.put("", "qux", "quux")
        self._request.assert_called_once_with("PUT",
            url=self._url.return_value, 
            auth=(self._user.return_value, self._pass.return_value),
            params="qux", data="quux", headers=None)

    def test_oauth_valid_bearer_token(self):
        with patch("time.time", return_value=1000):
            self._token.return_value = "access_token_1234"
            self._exp.return_value = 1000 + 3600
            self._client.delete("qux")
            self._request.assert_called_once_with(
                "DELETE",
                url="foo/qux",
                auth=ANY,
                params=None, data=None, headers=None)
            called_args, called_kwargs = self._request.call_args
            auth = called_kwargs["auth"]
            self.assertIsInstance(auth, BearerAuth)
            self.assertEqual(auth.token, "access_token_1234")

    def test_oauth_expired_token_no_client_credentials_uses_basic_auth(self):
        with patch("time.time", return_value=1000):
            self._token.return_value = "expired_token"
            self._exp.return_value = 500
            self._client.delete("qux")
            self._request.assert_called_once_with(
                "DELETE",
                url="foo/qux",
                auth=(self._user.return_value, self._pass.return_value),
                params=None, data=None, headers=None)

    def test_oauth_client_credentials_flow(self):
        with patch("time.time", return_value=1000):
            self._token.return_value = None
            self._exp.return_value = 0
            self._client_id.return_value = "client_id_abc"
            self._client_secret.return_value = "client_secret_xyz"
            with patch("bandwidth_numbers.client.Client._refresh_oauth_token",
                       return_value=BearerAuth("refreshed_token")) as refresh_mock:
                self._client.delete("qux")
                self._request.assert_called_once_with(
                    "DELETE",
                    url="foo/qux",
                    auth=ANY,
                    params=None, data=None, headers=None)

                called_args, called_kwargs = self._request.call_args
                auth = called_kwargs["auth"]
                self.assertIsInstance(auth, BearerAuth)
                self.assertEqual(auth.token, "refreshed_token")
                refresh_mock.assert_called_once()

if __name__ == "__main__":
    main()
