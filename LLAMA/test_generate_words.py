from unittest import TestCase
from generate_words import GenerateWords
from googletrans import Translator


class TestGenerateWords(TestCase):
    def setUp(self) -> None:
        self.min_len = 5
        self.max_len = 15
        self.generator = GenerateWords('es', self.min_len, self.max_len)
        self.translator = Translator()

    def test_generate_random_word_returns_a_string(self):
        out = self.generator.random()
        self.assertIsInstance(out, str)

    def test_google_translation(self):
        translation = self.translator.translate('squirrel', dest='fr').text
        print(translation)
        self.assertEquals(translation, "écureuil", "squirrel is écureuil in french")

    def test_can_generate_in_spanish(self):
        spanish_generator = GenerateWords('es')
        spanish_word = spanish_generator.random()
        translated_word = self.translator.translate(spanish_word, dest='en').text
        reverse_translation = self.translator.translate(translated_word, dest='es').text
        self.assertEquals(spanish_word, reverse_translation, f"Reverse translation doesn't match. The word '{spanish_word}' is different to {reverse_translation}. Generated word should be in Spanish")

<<<<<<< .mine



||||||| .r80
=======
    def test_words_respect_max_length(self):
        word = self.generator.random()
        self.assertLess(len(word), self.max_len,
                        f"The word '{word}' is should not be longer than max length ({self.max_len}).")

    def test_words_respect_min_length(self):
        word = self.generator.random()
        self.assertLess(self.min_len, len(word),
                        f"The word '{word}' is should be longer than min length ({self.min_len}).")
>>>>>>> .r92
