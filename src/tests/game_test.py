import unittest
from logic.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_insert_new_cell_fills_the_board(self):
        for i in range(16):
            self.game._insert_new_cell()

        state = self.game.get_gamestate()
        all_filled = True

        for i in range(len(state)):
            if None in state[i]:
                all_filled = False
                break

        self.assertEqual(all_filled, True)

    def test_new_keypress_accepts_only_valid_presses(self):
        result = self.game.new_keypress("123")
        self.assertEqual(result, False)
        result = self.game.new_keypress("updown")
        self.assertEqual(result, False)

    def test_game_accepts_valid_keypresses(self):
        result = self.game.new_keypress("up")
        self.assertEqual(result, True)
        result = self.game.new_keypress("left")
        self.assertEqual(result, True)
        result = self.game.new_keypress("down")
        self.assertEqual(result, True)
        result = self.game.new_keypress("right")
        self.assertEqual(result, True)