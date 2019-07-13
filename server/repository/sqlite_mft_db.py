import os
import sqlite3
from contextlib import closing
from typing import List, Dict

from model.lens import Lens
from repository.i_mft_db import IMftDb


class SQLiteMftDb(IMftDb):
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), '..', 'database', '.sqlite')

    def get_lenses(self) -> List[Lens]:
        connect = closing(sqlite3.connect(self.file_path))
        cursor = connect.thing.cursor()
        query = "SELECT node_field_data.title, node__field_official_link.field_official_link_uri FROM  node_field_data," \
                "node__field_official_link WHERE node_field_data.nid= node__field_official_link.entity_id AND " \
                "node_field_data.type='lens'"
        return [Lens(name=row[0], official_link=row[1]) for row in cursor.execute(query)]
