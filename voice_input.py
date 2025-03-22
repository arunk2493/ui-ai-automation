import speech_recognition as sr

def capture_voice_input(language="en"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for test case...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print(f"Recognized Command: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError:
        print("Speech recognition service error")
        return None
