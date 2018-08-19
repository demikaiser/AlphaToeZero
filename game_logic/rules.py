# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import unittest


def is_game_terminated(state):
    """Determines if the game is terminated at this state.

    Returns:
        True if the game can continue from the current state.
    """

    if not is_there_empty_board(state):
        return True

    winner = get_winner(state)

    if winner == 1 or winner == -1:
        return True

    return False


def is_there_empty_board(state):
    """Determines if the board has a empty spot to proceed.

    Returns:
        True if there is at least one empty board spot.
    """

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return True
    return False


def get_winner(state):
    """Determines the winner of the game if possible.

    Returns:
        A integer number indicating the winner of the game. 1 means the
        player O, -1 means the player X, 0 means no winner yet.
    """

    sums = []

    sum_row_0 = state[0][0] \
                + state[0][1] \
                + state[0][2]
    sums.append(sum_row_0)

    sum_row_1 = state[1][0] \
                + state[1][1] \
                + state[1][2]
    sums.append(sum_row_1)

    sum_row_2 = state[2][0] \
                + state[2][1] \
                + state[2][2]
    sums.append(sum_row_2)

    sum_col_0 = state[0][0] \
                + state[1][0] \
                + state[2][0]
    sums.append(sum_col_0)

    sum_col_1 = state[0][1] \
                + state[1][1] \
                + state[2][1]
    sums.append(sum_col_1)

    sum_col_2 = state[0][2] \
                + state[1][2] \
                + state[2][2]
    sums.append(sum_col_2)

    sum_cross_0 = state[0][0] \
                  + state[1][1] \
                  + state[2][2]
    sums.append(sum_cross_0)

    sum_cross_1 = state[0][2] \
                  + state[1][1] \
                  + state[2][0]
    sums.append(sum_cross_1)

    for i in sums:
        if i == 3:
            return 1
        elif i == -3:
            return -1

    return 0

def is_this_all_empty_board(state):
    """Determines if all the board spots are empty.

    Returns:
        True if there are 9 empty spots.
    """

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                return False
    return True

class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        print('Unit Test 0000 Executed!')


if __name__ == '__main__':
    unittest.main()