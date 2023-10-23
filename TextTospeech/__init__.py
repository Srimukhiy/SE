import pyttsx3

def text_to_speech(text):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        engine.setProperty("rate", 150)
        # Convert the text to speech
        engine.say(text)

        # Play the speech
        engine.runAndWait()

    except Exception as e:
        print(f"An error occurred: {e}")



