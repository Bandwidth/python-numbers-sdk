#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.note import NoteData

XPATH_NOTE = ""

class Note(BaseResource, NoteData):

    """Order notes"""

    _save_post = True
    _xpath = XPATH_NOTE
    _xpath_save = _xpath

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)

    def save(self):
        self.user_id = self.client.config.username
        self._save()
