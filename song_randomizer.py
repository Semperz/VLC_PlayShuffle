if __name__ == '__main__':
    from src.randomize_list import randomize_xspf
    from src.extract_data_xml import parse_xspf
    from src.path_maker import path_maker

if __name__ != '__main__':
    from .src.randomize_list import randomize_xspf
    from .src.extract_data_xml import parse_xspf
    from .src.path_maker import path_maker

def song_randomizer(root):
    import subprocess
    assert root.endswith('.xspf')
    assert isinstance(root,str)
    songs_path = parse_xspf(root)
    random_order_songs = randomize_xspf(songs_path)
    vlc_execution = path_maker(random_order_songs)
    assert isinstance(vlc_execution, list)
    return subprocess.run(vlc_execution)

song_randomizer('media/playlist.xspf')