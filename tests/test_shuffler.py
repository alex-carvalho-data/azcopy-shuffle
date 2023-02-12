from datetime import datetime
from pathlib import PurePath

from azcopy_shuffle.shuffler import CopyMap


# Instantiate an FileShuffling object with file_name, source_path
# and last_upd fields
def test_copy_map_instantiation() -> None:
    sample_dir = '/some_dir/something/'
    sample_file_name = 'file_x.txt'
    source_path = PurePath(sample_dir + sample_file_name)

    copy_map = CopyMap(source_path, datetime.now())
    assert isinstance(copy_map, CopyMap)
    assert copy_map.source_path == source_path
    assert copy_map.file_name == sample_file_name
