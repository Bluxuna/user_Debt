import pyttsx3


def text_to_speech(text):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_dict = {'Male': 0, 'Female': 1}
    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 1)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')

    engine.say(text)
    engine.runAndWait()