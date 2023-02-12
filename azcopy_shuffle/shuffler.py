from datetime import datetime
from pathlib import PurePath


class CopyMap:
    def __init__(self, source_path: PurePath, last_upd: datetime):
        self.source_path = source_path
        self.last_upd = last_upd

    @property
    def file_name(self) -> str:
        return self.source_path.name
