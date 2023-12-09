from src.extract_data_xml import parse_xspf
import xml.etree.ElementTree as ET
import pytest

@pytest.mark.invalid_format
def test_invalid_format():
    with pytest.raises(ET.ParseError):
        parse_xspf('test/invalid_xspf.xspf')