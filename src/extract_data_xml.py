import xml.etree.ElementTree as ET
def parse_xspf(file):
    try:
        assert file.endswith('.xspf') == True
        parsed_xspf = ET.parse(file)
        root_xspf = parsed_xspf.getroot()
        xspf_list = []
        for track in root_xspf.iter('{http://xspf.org/ns/0/}track'):
            location = track.find('{http://xspf.org/ns/0/}location').text
            xspf_list.append(location)
        return xspf_list
    except ET.ParseError as failedParse:
        print(f'Error parsing xspf file:{failedParse}')
        return None
    except AssertionError as notListError:
        print(f'Error: {notListError}')
        return None