from generate_words import GenerateWords
from Text_To_Speech import TextToSpeech
import pygame

pygame.mixer.init()


class GameRound:
    def __init__(self, number, word):
        self.number = number
        self.word = word


class Game:
    def __init__(self, language='en-GB', difficulty='Easy'):
        self.good_sound = pygame.mixer.Sound('good.wav')

        self.language = language
        self.min_word_len = 1
        self.max_word_len = 4

        self.rounds = 1
        self.difficulty = difficulty
        self.configure_difficulty(difficulty)

        self.current_round = 0
        self.total_points = 0

        self.word_generator = GenerateWords(self.language, self.min_word_len, self.max_word_len)

        self.text_to_speech = TextToSpeech(language=self.language)

    def get_next_round(self, answer=None):
        if answer is not None:
            self.submit_answer(answer)
        self.current_round += 1
        word_this_round = self.word_generator.random()
        return GameRound(self.current_round, word_this_round)

    def pronounce_word(self, word):
        self.text_to_speech.speak(word)

    def submit_answer(self, answer):
        Game.validate_answer(answer, self)
        if answer == "Bad":
            self.total_points += 1
        elif answer == "Okay":
            self.total_points += 2
        elif answer == "Good":
            self.total_points += 3

    def configure_difficulty(self, difficulty):
        Game.validate_difficulty(difficulty)

        if difficulty == "Easy":
            self.rounds = 3
            self.min_word_len = 2
            self.max_word_len = 4
        elif difficulty == "Medium":
            self.rounds = 5
            self.min_word_len = 5
            self.max_word_len = 6
        elif difficulty == "Hard":
            self.rounds = 10
            self.min_word_len = 7
            self.max_word_len = 10

    @staticmethod
    def validate_difficulty(difficulty):
        if not isinstance(difficulty, str):
            raise ValueError("Difficulty must be a string")
        if difficulty not in ["Easy", "Medium", "Hard"]:
            raise ValueError("Difficulty must be one of 'Easy', 'Medium', 'Hard'")

    @staticmethod
    def validate_answer(answer, game):
        if not isinstance(answer, str):
            raise ValueError("Answer must be a string")
        if answer not in ['Bad', 'Okay', 'Good']:
            raise ValueError("Answer must be one of 'Bad', 'Okay', 'Good'")

        if answer == "Good":
            game.good_sound.play()
