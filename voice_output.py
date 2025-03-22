import pyttsx3 # type: ignore

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()