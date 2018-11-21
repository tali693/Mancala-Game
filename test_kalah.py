from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6, 4)

    def test_1_1_initial_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_1_1_illegal_hole(self):
        first_bank = (len(self.game.status()) - 2) / 2
        self.assertRaises(IndexError, self.game.play, -1)
        self.assertRaises(IndexError, self.game.play, 100)
        self.assertRaises(IndexError, self.game.play, first_bank)
        self.assertRaises(IndexError, self.game.play, first_bank * 2 + 1)

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

    def test_1_2_crossing_other_bank(self):
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
        self.assertEqual(self.game.play(7), "Player 1 plays next")
        self.assertEqual(self.game.status(), (5, 1, 6, 0, 1, 7, 2, 0, 8, 7, 5, 0, 5, 1))
        self.assertEqual(self.game.play(4), "Player 2 plays next")
        self.assertEqual(self.game.status(), (5, 1, 6, 0, 0, 8, 2, 0, 8, 7, 5, 0, 5, 1))
        self.assertEqual(self.game.play(12), "Player 1 plays next")
        self.assertEqual(self.game.status(), (6, 2, 7, 1, 0, 8, 2, 0, 8, 7, 5, 0, 0, 2))
        self.assertEqual(self.game.play(5), "Player 2 plays next")
        self.assertEqual(self.game.status(), (7, 2, 7, 1, 0, 0, 3, 1, 9, 8, 6, 1, 1, 2))

    def test_1_2_empty_hole(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(7), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 4, 0))
        self.assertRaises(ValueError, self.game.play, 1)

    def test_1_3_bonus_move_player_1(self):
        self.assertEqual(self.game.play(2), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0))

    def test_1_3_bonus_move_player_2(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(9), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 0, 5, 5, 5, 1))

    def test_1_4_capture_player_1(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(8), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))
        self.assertEqual(self.game.play(4), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 5, 1, 6, 5, 5, 5, 0))
        self.assertEqual(self.game.play(7), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 0, 2, 7, 6, 6, 6, 0))
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 1, 6, 6, 0, 6, 4, 0, 0, 7, 6, 6, 6, 0))

    def test_1_4_capture_player_2(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(8), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))
        self.assertEqual(self.game.play(4), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 5, 1, 6, 5, 5, 5, 0))
        self.assertEqual(self.game.play(7), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 0, 2, 7, 6, 6, 6, 0))
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 1, 6, 6, 0, 6, 4, 0, 0, 7, 6, 6, 6, 0))

    def test_1_4_non_capture(self):
        self.assertEqual(self.game.play(1), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(8), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0))
        self.assertEqual(self.game.play(4), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 5, 1, 6, 5, 5, 5, 0))
        self.assertEqual(self.game.play(8), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 0, 5, 5, 0, 6, 1, 5, 0, 7, 5, 5, 5, 0))
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 1, 6, 6, 1, 6, 1, 5, 0, 7, 5, 5, 5, 0))


#    (12, 11, 10,  9, 8, 7)
# 13                        6
#    (0,   1,  2,  3, 4, 5)

if __name__ == '__main__':
    unittest.main()
