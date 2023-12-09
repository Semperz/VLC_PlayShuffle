from src.randomize_list import randomize_xspf
import pytest

@pytest.mark.empty_list
def test_empty_list():
    assert randomize_xspf([]) == []