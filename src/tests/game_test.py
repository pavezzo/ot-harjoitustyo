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