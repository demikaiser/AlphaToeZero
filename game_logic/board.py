# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>


import unittest

import numpy as np


class Board(object):

    def __init__(self):
        self.state = np.array([[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]],
                              dtype=np.int8)


class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        print('Unit Test 0000 Executed!')
        board = Board()
        print(board.state)

        for i in range(3):
            for j in range(3):
                print(board.state[i][j])


if __name__ == '__main__':
    unittest.main()