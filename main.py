import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import musicLibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open snapchat" in c.lower():
        webbrowser.open("https://snapchat.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    speak("Inishilizing jarvis in a terminal")
    while True:
        # listen for the wake word "jarvis"
        #obtain audio from the mic
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listning..   !")
                audio = r.listen(source)
            # recognize speech using google
            word = r.recognize_google(audio)
            if (word.lower() == "hey jarvis"):
                speak("Ya i am listening..!")
            #listning orders
                with sr.Microphone() as source:
                    print("JARVIS active...  !")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)




        except Exception as e:
            print(" error; {0}".format(e))
