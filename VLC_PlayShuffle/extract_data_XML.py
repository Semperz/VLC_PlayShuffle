import xml.etree.ElementTree as ET

def parse_xspf(parsed):
    tree = ET.parse('playlistVLC.xspf')
    root = tree.getroot()
