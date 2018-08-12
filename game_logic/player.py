# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import unittest


class Player(object):

    def __init__(self, agent, side):
        self.agent = agent  # "Human" | "AI with Search" | "AI with Learning"
        self.side = side  # 1 | -1


class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        print('Unit Test 0000 Executed!')


if __name__ == '__main__':
    unittest.main()