from src.randomize_list import randomize_xspf
from src.extract_data_xml import parse_xspf
import pytest

@pytest.mark.same_length
def test_same_length():
    xspf_file = 'media/playlist.xspf'
    original_list = parse_xspf(xspf_file)
    random_list = randomize_xspf(original_list)
    assert len(original_list) == len(random_list)