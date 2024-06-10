#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData, BaseResourceList
from bandwidth_numbers.models.note import Note
from bandwidth_numbers.models.maps.notes import NotesMap

class NotesData(NotesMap, BaseData):

    def __init__(self, parent=None):
        self.note = BaseResourceList(Note, parent)
