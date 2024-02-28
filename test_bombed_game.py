import unittest
from laberinto import BombedGame

class TestBombedGame(unittest.TestCase):

    def test_init(self):
        game = BombedGame()
        self.assertEqual(game.rows, 10)
        self.assertEqual(game.cols, 10)
        self.assertEqual(game.bombs, 10)

    def test_is_valid_move(self):
        game = BombedGame()
        self.assertTrue(game.is_valid_move(0, 0))
        self.assertFalse(game.is_valid_move(-1, 0))
        self.assertFalse(game.is_valid_move(0, -1))
        self.assertFalse(game.is_valid_move(10, 0))
        self.assertFalse(game.is_valid_move(0, 10))

    def test_make_move(self):
        game = BombedGame()
        game.make_move(0, 0)
        self.assertEqual(game.board[0][0], 1)
        with self.assertRaises(ValueError):
            game.make_move(-1, 0)
        with self.assertRaises(ValueError):
            game.make_move(0, -1)
        with self.assertRaises(ValueError):
            game.make_move(10, 0)
        with self.assertRaises(ValueError):
            game.make_move(0, 10)

    def test_is_game_over(self):
        game = BombedGame()
        self.assertFalse(game.is_game_over())
        game.board[0][0] = -1
        self.assertTrue(game.is_game_over())
