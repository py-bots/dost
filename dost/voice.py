"""
Voice Module for dost.This module contains all the functions related to voice recognition and text to speech.

Examples:
    >>> from dost import voice
    >>> voice.text_to_speech(text="Hello World")
    

This module contains the following functions:
        
- `speech_to_text()`: Converts speech to text.
- `text_to_speech(text, show, rate)`: Converts text to speech.
"""


from dost.helpers import dostify


@dostify(errors=[(Exception, "Could not find PyAudio or no Microphone input device found. It may be being used by another application.")])
def speech_to_text() -> str:
    """ 
    Converts speech to text
    Returns:
        string: Text from the speech
    Examples:
        >>> voice.speech_to_text()
        "Hello World"
    """
    # Import Section
    from dost.helpers import make_sure_pyaudio_is_installed
    import speech_recognition as sr

    # Code Section
    make_sure_pyaudio_is_installed()
    recognizer = sr.Recognizer()
    energy_threshold = [3000]

    unknown = False
    data = None

    while True:
        with sr.Microphone() as source:
            recognizer.dynamic_energy_threshold = True
            if recognizer.energy_threshold in energy_threshold or recognizer.energy_threshold <= \
                    sorted(energy_threshold)[-1]:
                recognizer.energy_threshold = sorted(
                    energy_threshold)[-1]
            else:
                energy_threshold.append(
                    recognizer.energy_threshold)

            recognizer.pause_threshold = 0.8

            recognizer.adjust_for_ambient_noise(source)

            try:
                if not unknown:
                    text_to_speech("Speak now")
                audio = recognizer.listen(source)
                return recognizer.recognize_google(audio)
            except AttributeError:
                text_to_speech(
                    "Could not find PyAudio or no Microphone input device found. It may be being used by "
                    "another "
                    "application.")
            except sr.UnknownValueError:
                unknown = True
            except sr.RequestError as e:
                print("Try Again")


@dostify(errors=[(Exception, "Could not find PyAudio or no Microphone input device found. It may be being used by another application.")])
def text_to_speech(text: str, show: bool = True, rate: int = 170) -> None:
    """
    Converts text to speech offline
    Args:
        text (string): Text to be converted to speech
        show (bool): Whether to print the text or not
        rate (int): Rate of speech. Default is 170
    Examples:
        >>> voice.text_to_speech(text="Hello World")
    """
    # Import Section
    import random
    import pyttsx3
    from dost.helpers import _is_speaker_available
    if _is_speaker_available():
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        voice = random.choice(voices)  # Randomly decide male/female voice
        engine.setProperty('voice', voice.id)

        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()
    else:
        print("Speaker not connected")

    if show:
        if type(text) is list:
            print(' '.join(text))
        else:
            print(text)
