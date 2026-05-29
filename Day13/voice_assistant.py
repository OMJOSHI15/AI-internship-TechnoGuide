import speech_recognition as sr
import pyttsx3

# Text to speech
engine = pyttsx3.init()

# Speech recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("Listening...")

    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        print("You said:", text)

        response = "You said " + text

        engine.say(response)
        engine.runAndWait()

    except:
        print("Sorry, could not understand")