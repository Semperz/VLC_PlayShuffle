import subprocess
import platform

def call_vlc():
    if platform.system() == "Windows":
        command = ["\VLC\VLC.exe"]
    elif platform.system() == "Darwin": #macOS
        command = ["open", "-a", "VLC"]
    else:  #Linux
        command = ["vlc"]

    subprocess.run(command)

if __name__ == "__main__":
    call_vlc()