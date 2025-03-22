import speech_recognition as sr # type: ignore
import pyaudio # type: ignore

def list_audio_devices():
    """ Lists available audio input devices (microphone, headset, Bluetooth). """
    p = pyaudio.PyAudio()
    device_list = []
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_info["maxInputChannels"] > 0:  # Input devices only
            device_list.append((i, device_info["name"]))
    p.terminate()
    return device_list

def capture_voice_command(device_index=None):
    """
    Captures voice input from the selected device (Microphone, Wired, or Bluetooth).
    - If `device_index` is None, it defaults to the system microphone.
    - Otherwise, it uses the specified audio input device.
    """
    recognizer = sr.Recognizer()
    device_list = list_audio_devices()

    if device_index is None:
        print("No device index provided. Using the system default microphone.")
    else:
        print(f"Using input device: {device_list[device_index][1]}")

    try:
        with sr.Microphone(device_index=device_index) as source:
            print("Listening for test scenario...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"Captured Voice Command: {command}")
            return command
    except sr.UnknownValueError:
        print("Could not understand voice input.")
        return None
    except sr.RequestError:
        print("Speech Recognition service error.")
        return None
    except Exception as e:
        print(f"Error capturing voice input: {e}")
        return None

if __name__ == "__main__":
    # List available audio devices
    devices = list_audio_devices()
    for i, name in devices:
        print(f"[{i}] {name}")

    # Capture voice command using the first available device
    if devices:
        print("\nUsing the first detected audio device for voice input...")
        capture_voice_command(devices[0][0])
    else:
        print("No audio input devices found.")
