from gtts import gTTS
from io import BytesIO
import pygame
from PyDictionary import PyDictionary


def filter_oxford_dictionary(blacklist):
    dictionary = PyDictionary("en")
    english_dictionary = dictionary.get_oxford_dict()
    filtered_dictionary = {word: definition for word, definition in english_dictionary.items() if
                           word.lower() not in blacklist}
    return filtered_dictionary


class TextToSpeech:
    def __init__(self, language='en', profanity_blacklist=None):
        self.language = language
        self.profanity_blacklist = profanity_blacklist or []

    def speak(self, text):
        tts = gTTS(text, lang=self.language)
        mp3_fo = BytesIO()
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(mp3_fo)

        # Check if any profanity words are in the text before playing
        if any(word.lower() in self.profanity_blacklist for word in text.split()):
            print("Profanity detected. Text not spoken.")
            return

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


profanity_blacklist = ['X', 'XX', 'XXX', 'XXXX']

tts = TextToSpeech(language='en', profanity_blacklist=profanity_blacklist)
text_to_speak = "This is an example sentence with X, XX, XXX, and XXXX."

tts.speak(text_to_speak)
