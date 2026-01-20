import webbrowser
import musicLibrary
from app.speech.text_to_speech import speak

def process_command(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")

    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "open snapchat" in command:
        webbrowser.open("https://snapchat.com")

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")

    elif command.startswith("play"):
        song = command.split(" ")[1]
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found")
