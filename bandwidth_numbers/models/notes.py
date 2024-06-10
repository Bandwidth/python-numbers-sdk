#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from bandwidth_numbers.models.base_resource import BaseResource
from bandwidth_numbers.models.data.notes import NotesData
from bandwidth_numbers.models.note import Note

XPATH_NOTES = "/notes"

class Notes(BaseResource, NotesData):

    """Order notes"""

    _save_post = True
    _xpath = XPATH_NOTES
    _xpath_save = _xpath

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        NotesData.__init__(self, self)

    def create(self, data=None, save=True):
        note = Note(self).set_from_dict(data)
        if save and (data is not None):
            note.save()
        return note

    def list(self):
        return self._get_data().note
