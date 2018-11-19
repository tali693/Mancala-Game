from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6, 4)

    def test_1_1_initial_status(self):

        self.assertEqual(self.game.get_board(), [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])

    def test_1_1_illegal_hole(self):
        self.assertRaises(IndexError, self.game.play, -1)
        self.assertRaises(IndexError, self.game.play, -2)
        self.assertRaises(IndexError, self.game.play, 14)
        self.assertRaises(IndexError, self.game.play, 20)

    def test_1_2_simple_move(self):
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.play(8), "Player 1 plays next")

if __name__ == '__main__':
    unittest.main()
