from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6, 4)

    def test_1_1_initial_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_1_1_illegal_hole(self):
        self.assertRaises(IndexError, self.game.play, -1)
        self.assertRaises(IndexError, self.game.play, -2)
        self.assertRaises(IndexError, self.game.play, 14)
        self.assertRaises(IndexError, self.game.play, 20)

    def test_1_2_simple_move(self):
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(8), "Player 1 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 0, 5, 5, 5, 5, 0))

    def test_1_2_crossing_move(self):
        self.assertEqual(self.game.play(3), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 1, 5, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(12), "Player 1 plays next")
        self.assertEqual(self.game.status(), (5, 5, 5, 0, 5, 5, 1, 5, 4, 4, 4, 4, 0, 1))
        self.assertEqual(self.game.play(5), "Player 2 plays next")
        self.assertEqual(self.game.status(), (5, 5, 5, 0, 5, 0, 2, 6, 5, 5, 5, 4, 0, 1))

    def test_1_2_two_simple_moves(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(8), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))

    def test_1_2_player_2_crosses(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(7), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 4, 0))
        self.assertEqual(self.game.play(4), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 1, 6, 6, 5, 5, 4, 0))
        self.assertEqual(self.game.play(11), "Player 1 plays next")
        self.assertEqual(self.game.status(), (5, 1, 6, 5, 0, 6, 1, 1, 6, 6, 5, 0, 5, 1))
        self.assertEqual(self.game.play(3), "Player 2 plays next")
        self.assertEqual(self.game.status(), (5, 1, 6, 0, 1, 7, 2, 2, 7, 6, 5, 0, 5, 1))

if __name__ == '__main__':
    unittest.main()
