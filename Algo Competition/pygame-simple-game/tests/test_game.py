import unittest
from src.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initialization(self):
        self.assertIsNotNone(self.game)
        self.assertEqual(self.game.state, 'menu')

    def test_start_game(self):
        self.game.start_game()
        self.assertEqual(self.game.state, 'play')

    def test_game_over(self):
        self.game.start_game()
        self.game.game_over()
        self.assertEqual(self.game.state, 'game_over')

    def test_score_increment(self):
        initial_score = self.game.score
        self.game.increment_score(10)
        self.assertEqual(self.game.score, initial_score + 10)

    def test_reset_game(self):
        self.game.start_game()
        self.game.reset_game()
        self.assertEqual(self.game.state, 'menu')
        self.assertEqual(self.game.score, 0)

if __name__ == '__main__':
    unittest.main()