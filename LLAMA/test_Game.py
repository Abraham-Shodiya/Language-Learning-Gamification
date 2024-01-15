from unittest import TestCase
from Game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_get_next_round(self):
        new_round = self.game.get_next_round()
        self.assertEquals(new_round.number, 1, 'Round number should be 1')
        self.assertEquals(self.game.current_round, new_round.number,
                          'Round number should be equal with the current round of the game')
        self.assertIsInstance(new_round.word, str)

    def test_submit_answer(self):
        old_score = self.game.total_points
        self.game.submit_answer('Okay')
        self.assertLess(old_score, self.game.total_points, 'Score should increase when you answer Okay')

    def test_configure_difficulty(self):
        easy_game = Game(difficulty='Easy')
        hard_game = Game(difficulty='Hard')
        hard_word = hard_game.get_next_round().word

        self.assertLessEqual(easy_game.min_word_len, easy_game.max_word_len, 'Min len must be lower than max len')
        self.assertLess(easy_game.rounds, hard_game.rounds, 'Easier levels should have fewer rounds')
        self.assertLess(easy_game.max_word_len, hard_game.max_word_len, 'Easier levels should have shorter words')
        self.assertLessEqual(len(hard_word), hard_game.max_word_len, f'Word: {hard_word} is longer than max len')
        self.assertLessEqual(hard_game.min_word_len, len(hard_word),f'Word: {hard_word} is shorter than min len')

    def test_validate_difficulty(self):
        def attempt_to_validate_bad_input():
            Game.validate_difficulty('fake difficulty')

        self.failUnlessRaises(ValueError, attempt_to_validate_bad_input)

    def test_validate_answer(self):
        def attempt_to_validate_bad_input():
            Game.validate_answer('fake answer')

        self.failUnlessRaises(ValueError, attempt_to_validate_bad_input)
