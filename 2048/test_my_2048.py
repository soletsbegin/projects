import unittest
import my_2048


class My_2048_testcase(unittest.TestCase):

    def test_left(self):
        res1 = my_2048.left_move([[0, 0, 16, 0],
                                  [4, 4, 4,  4],
                                  [0, 0, 2,  2],
                                  [2, 4, 4,  0]])
        self.assertEqual(res1, [[16, 0, 0, 0],
                                [8,  8, 0, 0],
                                [4,  0, 0, 0],
                                [2,  8, 0, 0]])

    def test_right(self):
        res1 = my_2048.right_move([[0, 0, 16, 0],
                                   [4, 4, 0,  0],
                                   [0, 0, 2,  2],
                                   [2, 4, 4,  0]])
        self.assertEqual(res1, [[0, 0, 0, 16],
                                [0, 0, 0, 8],
                                [0, 0, 0, 4],
                                [0, 0, 2, 8]])

    def test_up(self):
        res1 = my_2048.up_move([[0, 0, 16, 0],
                                [4, 4, 0,  0],
                                [0, 0, 2,  2],
                                [2, 4, 4,  0]])
        self.assertEqual(res1, [[4, 8, 16, 2],
                                [2, 0, 2,  0],
                                [0, 0, 4,  0],
                                [0, 0, 0,  0]])

    def test_add_2(self):
        res = my_2048.add_2([[2, 2, 16, 0],
                             [4, 4, 2,  2],
                             [2, 2, 2,  2],
                             [2, 4, 4,  2]])
        self.assertEqual(res, [[2, 2, 16, 2],
                              [4, 4, 2, 2],
                              [2, 2, 2, 2],
                              [2, 4, 4, 2]])


if __name__ == "__main__":
    unittest.main()