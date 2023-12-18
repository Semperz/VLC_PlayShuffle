import platform
def path_maker(song_paths):
    assert isinstance(song_paths, list)
    if platform.system() == 'Windows':
        vlc_path = [r'C:\Program Files\VideoLAN\VLC\VLC.exe']  #Windows
    elif platform.system() == 'Darwin':
        vlc_path = [r'/Applications/VLC.app/Contents/MacOS/VLC']  #MacOS
    elif platform.system() == 'Linux':
        vlc_path = [r'/usr/bin/vlc']  #Linux
    else:
        raise NotImplementedError("Program is not supported on the current operating system.")

    vlc_path.extend(song_paths)
    assert isinstance(vlc_path, list)
    return vlc_path
