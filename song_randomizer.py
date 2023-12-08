from src.randomize_list import randomize_xspf
from src.extract_data_xml import parse_xspf
from src.path_maker import path_maker
import subprocess
def song_randomizer(root):
    songs_path = parse_xspf(root)
    random_order_songs = randomize_xspf(songs_path)
    vlc_execution = path_maker(random_order_songs)
    return subprocess.run(vlc_execution)

print(song_randomizer('playlist.xspf'))
