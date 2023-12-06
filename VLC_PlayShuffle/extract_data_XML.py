import xml.etree.ElementTree as ET
def extract_xspf_list():
    parsed_xspf = ET.parse('playlistVLC.xspf')
    root_xspf = parsed_xspf.getroot()
    xspf_list =[]
    for track in root_xspf.iter('{http://xspf.org/ns/0/}track'):
        location = track.find('{http://xspf.org/ns/0/}location').text
        xspf_list.append(location)
    return xspf_list

