from app.speech.text_to_speech import speak
from app.speech.speech_to_text import listen
from app.core.command_processor import process_command

def main():
    speak("Initializing Jarvis in a terminal")

    while True:
        try:
            print("Waiting for wake word...")
            word = listen()

            if word.lower() == "hey jarvis":
                speak("Yes, I am listening")

                command = listen()
                process_command(command)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
