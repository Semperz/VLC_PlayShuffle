from src.extract_data_xml import parse_xspf
import xml.etree.ElementTree as ET
import pytest

@pytest.mark.empty_file
def test_empty_file():
    with pytest.raises(ET.ParseError):
        parse_xspf('test/empty_xspf_file.xspf')
