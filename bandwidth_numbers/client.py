#!/usr/bin/env python

import time
from bandwidth_numbers.utils.config import Config
from bandwidth_numbers.utils.rest import RestClient
from bandwidth_numbers.utils.bearer_auth import BearerAuth

class Client(object):

    """HTTP requests"""

    @property
    def config(self):
        return self._config

    def __init__(
            self, url=None, account_id=None, username=None,
            password=None, filename=None, client_id=None,
            client_secret=None, access_token=None, access_token_expiration=int(time.time()) + 3600):

        if url is None:
            url = "https://dashboard.bandwidth.com/api"

        self._config = Config(url, account_id, username, password,
                              filename, client_id, client_secret,
                              access_token, access_token_expiration)
        self._rest = RestClient()

    def _get_uri(self, section=None):

        """http://foo/bar/// + ///bar/// -> http://foo/bar"""

        _section = ""
        if section is not None:
            _section = section.lstrip('/').rstrip('/')

        res = self.config.url.rstrip('/') + ("" if not _section else '/') + \
            _section

        return res
    
    def _configure_auth(self):
        now = int(time.time())
        if self.config.access_token and self.config.access_token_expiration > now + 60:
            return BearerAuth(self.config.access_token)
        else:
            return (self.config.username, self.config.password)

    def _request(self,method,section=None,params=None,data=None,headers=None):
        auth = self._configure_auth()
        return self._rest.request(
                    method, url=self._get_uri(section), auth=auth,
                    params=params, data=data, headers=headers)

    def delete(self, section=None):
        return self._request("DELETE", section)

    def get(self, section=None, params=None):
        return self._request("GET", section, params)

    def post(self, section=None, params=None, data=None, headers=None):
        return self._request("POST", section, params, data, headers)

    def put(self, section=None, params=None, data=None, headers=None):
        return self._request("PUT", section, params, data, headers)
