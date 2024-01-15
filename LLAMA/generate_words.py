from wonderwords import RandomWord
from googletrans import Translator


# the googletrans seems to have an issue closing the socket to it's servers, seems like it's a known issue
# TODO investigate how to fix it (maybe close socket in try catch)
class GenerateWords:
    def __init__(self, lang='en', min_len=5, max_len=15):
        self.generator = RandomWord()
        self.translator = Translator()
        self.target_language = lang
        self.min_len = min_len
        self.max_len = max_len

    def random(self):
        random_word = self.generator.random_words(1, word_max_length=self.max_len, word_min_length=self.min_len)[0]
        if self.target_language != 'en':
            try:
                translation = self.translator.translate(random_word, dest=self.target_language)
                random_word = translation.text
            except TypeError:
                print("Ups TypeError, trying again")
                self.random()

        return random_word
