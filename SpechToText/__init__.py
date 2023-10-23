import speech_recognition as sr
import pyaudio;
import streamlit as st;
def input():
# Initialize the recognizer
    r = sr.Recognizer()
    # Capture audio input using a microphone
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        audio = r.listen(source)

# Use the Google Web Speech API to convert the audio to text
    try:
        text = r.recognize_google(audio);
        print(f"You said: {text}");
        st.spinner();
        return str(text);
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
