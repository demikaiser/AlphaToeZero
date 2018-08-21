# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import time
import math
import unittest

from game_logic import rules


def make_move(context_gui, context_game, player_side, init_state):
    """ Executes the Minimax search and make a movement.

    Args:
        context_gui: GUI context reference.
        context_game: Main game object reference.
        player_side: The player who initiated this search.
        init_state: Initial state to start.
    """

    opponent_side = -1 * player_side

    # Measure the time for the search.
    time_start = time.time()

    row, col = minimax_decision(init_state, player_side, opponent_side)

    time_end = time.time()
    context_gui.function_console_print(
        "=> Search Time: {} second".format(time_end - time_start))

    context_game.make_movement(player_side, row, col)


def minimax_decision(state, player_side, opponent_side):
    """ Search the Minimax tree and make a decision.

    Args:
        state: Current state of the board.
        player_side: 1 is O, -1 is X.
        opponent_side: 1 is O, -1 is X.

    Returns:
        An action that consists of row and column.
    """

    row = -1
    col = -1

    utility_value = -math.inf

    # If the board is all empty, start from the center.
    if rules.is_this_all_empty_board(state):
        return 1, 1

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                state[i][j] = player_side
                temp = min_value(state, player_side, opponent_side)
                if temp > utility_value:
                    utility_value = temp
                    row = i
                    col = j
                state[i][j] = 0

    return row, col


def max_value(state, player_side, opponent_side):
    """ Gets Minimax's maximum value.

    Args:
        state: Current state of the board.
        player_side: 1 is O, -1 is X.
        opponent_side: 1 is O, -1 is X.

    Returns:
        The maximum value in the Minimax function.
    """

    utility_value = -math.inf

    if rules.is_game_terminated(state):
        winner = rules.get_winner(state)
        if winner == player_side:
            return 10
        elif winner == opponent_side:
            return -10
        else:
            return 0

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                state[i][j] = player_side
                utility_value = max(utility_value,
                                    min_value(state,
                                              player_side,
                                              opponent_side))
                state[i][j] = 0

    return utility_value


def min_value(state, player_side, opponent_side):
    """ Gets Minimax's minimum value.

    Args:
        state: Current state of the board.
        player_side: 1 is O, -1 is X.
        opponent_side: 1 is O, -1 is X.

    Returns:
        The minimum value in the Minimax function.
    """

    utility_value = math.inf

    if rules.is_game_terminated(state):
        winner = rules.get_winner(state)
        if winner == player_side:
            return 10
        elif winner == opponent_side:
            return -10
        else:
            return 0

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                state[i][j] = opponent_side
                utility_value = min(utility_value,
                                    max_value(state,
                                              player_side,
                                              opponent_side))
                state[i][j] = 0

    return utility_value


class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        print('Unit Test 0000 Executed!')


if __name__ == '__main__':
    unittest.main()