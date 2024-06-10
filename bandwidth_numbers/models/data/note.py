#!/usr/bin/env python

from bandwidth_numbers.models.base_resource import BaseData
from bandwidth_numbers.models.maps.note import NoteMap

class NoteData(NoteMap, BaseData):
    pass
