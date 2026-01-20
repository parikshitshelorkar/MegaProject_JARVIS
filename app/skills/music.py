import webbrowser
import musicLibrary

def play_song(song):
    if song in musicLibrary.music:
        webbrowser.open(musicLibrary.music[song])
