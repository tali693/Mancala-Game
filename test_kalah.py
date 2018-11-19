from kalah import Kalah
import unittest


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6, 4)

    def test_1_1_initial_status(self):

        self.assertEqual(self.game.get_board(), [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])


if __name__ == '__main__':
    unittest.main()
