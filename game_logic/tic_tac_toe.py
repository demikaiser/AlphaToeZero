# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import unittest

from game_logic import board
from game_logic import player
from game_logic import ai_interface

class TicTacToe(object):
    """TicTacToe game container that has a board and two players.
    """

    def __init__(self, player_o_agent, player_x_agent, context):
        self.board = board.Board()
        self.player_o = player.Player(player_o_agent, 1)
        self.player_x = player.Player(player_x_agent, -1)
        self.turn = 1  # Initialized to 1, then -1, 1, -1, 1...
        self.context_gui = context  # GUI context for sending messages.

    def change_turn(self):
        """Changes the turn after a movement.
        """
        if self.turn == 1:
            self.turn = -1
            self.start_thinking_player_x()
        elif self.turn == -1:
            self.turn = 1
            self.start_thinking_player_o()

    def start_thinking_player_o(self):
        """ Makes the player O think.
        """

        if self.player_o.agent == "Human":
            self.context_gui.function_console_print("<Human O Player's Turn>")

        elif self.player_o.agent == "AI with Search":
            self.context_gui.function_console_print("<AI Search O Player's Turn>")
            ai_interface.AIInterface(self.context_gui, self, 1,
                                     self.board.state).generate_next_move()

        elif self.player_o.agent == "AI with Learning":
            self.context_gui.function_console_print("<AI Learning O Player's Turn>")
            ai_interface.AIInterface(self.context_gui, self, 1,
                                     self.board.state).generate_next_move()

    def start_thinking_player_x(self):
        """ Makes the player X think.
        """

        if self.player_x.agent == "Human":
            self.context_gui.function_console_print("<Human X Player's Turn>")

        elif self.player_x.agent == "AI with Search":
            self.context_gui.function_console_print("<AI Search X Player's Turn>")
            ai_interface.AIInterface(self.context_gui, self, -1,
                                     self.board.state).generate_next_move()

        elif self.player_x.agent == "AI with Learning":
            self.context_gui.function_console_print("<AI Learning X Player's Turn>")
            ai_interface.AIInterface(self.context_gui, self, -1,
                                     self.board.state).generate_next_move()

    def make_movement(self, player_side, row, col):
        """Makes a move for the given player.

        Args:
            player_side: Which player's move.
            row: Row number of the movement.
            col: Column number of the movement.
        """

        # Check if this is a legal move.
        if self.board.state[row][col] != 0:
            self.context_gui.function_console_print("Illegal move, do it again.")
            if player_side == 1 and "AI" in self.player_o.agent:
                self.start_thinking_player_o()
            elif player_side == -1 and "AI" in self.player_x.agent:
                self.start_thinking_player_x()
            return

        # Print the message about the movement.
        if self.turn == 1:
            self.context_gui.function_console_print("{} O moved at ({}, {})"
                                                    .format(self.player_o.agent,
                                                        row, col))
        elif self.turn == -1:
            self.context_gui.function_console_print("{} X moved at ({}, {})"
                                                    .format(self.player_o.agent,
                                                        row, col))

        if player_side == 1:
            self.board.state[row][col] = 1
        elif player_side == -1:
            self.board.state[row][col] = -1

        self.context_gui.update_buttonGameTiles()

        if self.is_game_terminated():
            self.context_gui.terminate_game(self.get_winner())
            return

        self.change_turn()

    def is_game_terminated(self):
        """Determines if the game is terminated at this state.

        Returns:
            True if the game can continue from the current state.
        """

        if not self.is_there_empty_board():
            return True

        winner = self.get_winner()

        if winner == 1 or winner == -1:
            return True

        return False

    def is_there_empty_board(self):
        """Determines if the board has a empty spot to proceed.

        Returns:
            True if there is at least one empty board spot.
        """

        for i in range(3):
            for j in range(3):
                if self.board.state[i][j] == 0:
                    return True
        return False

    def get_winner(self):
        """Determines the winner of the game if possible.

        Returns:
            A integer number indicating the winner of the game. 1 means the
            player O, -1 means the player X, 0 means no winner yet.
        """

        sums = []

        sum_row_0 = self.board.state[0][0] \
                  + self.board.state[0][1] \
                  + self.board.state[0][2]
        sums.append(sum_row_0)

        sum_row_1 = self.board.state[1][0] \
                  + self.board.state[1][1] \
                  + self.board.state[1][2]
        sums.append(sum_row_1)

        sum_row_2 = self.board.state[2][0] \
                  + self.board.state[2][1] \
                  + self.board.state[2][2]
        sums.append(sum_row_2)

        sum_col_0 = self.board.state[0][0] \
                  + self.board.state[1][0] \
                  + self.board.state[2][0]
        sums.append(sum_col_0)

        sum_col_1 = self.board.state[0][1] \
                  + self.board.state[1][1] \
                  + self.board.state[2][1]
        sums.append(sum_col_1)

        sum_col_2 = self.board.state[0][2] \
                  + self.board.state[1][2] \
                  + self.board.state[2][2]
        sums.append(sum_col_2)

        sum_cross_0 = self.board.state[0][0] \
                    + self.board.state[1][1] \
                    + self.board.state[2][2]
        sums.append(sum_cross_0)

        sum_cross_1 = self.board.state[0][2] \
                    + self.board.state[1][1] \
                    + self.board.state[2][0]
        sums.append(sum_cross_1)

        for i in sums:
            if i == 3:
                return 1
            elif i == -3:
                return -1

        return 0


class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        game = TicTacToe("", "", "", "")
        for i in range(3):
            for j in range(3):
                game.board.state[i][j] = 1

        self.assertFalse(game.is_there_empty_board())

    def test_case_0001(self):
        game = TicTacToe("", "", "", "")
        for i in range(3):
            for j in range(3):
                game.board.state[i][j] = 0

        self.assertTrue(game.is_there_empty_board())

    def test_case_0002(self):
        game = TicTacToe("", "", "", "")
        for i in range(3):
            for j in range(3):
                game.board.state[i][j] = 0

        self.assertEqual(0, game.get_winner())

    def test_case_0003(self):
        game = TicTacToe("", "", "", "")
        for i in range(3):
            for j in range(3):
                game.board.state[i][j] = 1

        self.assertEqual(1, game.get_winner())

    def test_case_0004(self):
        game = TicTacToe("", "", "", "")
        for i in range(3):
            for j in range(3):
                game.board.state[i][j] = -1

        self.assertEqual(-1, game.get_winner())

    def test_case_0005(self):
        game = TicTacToe("", "", "", "")
        game.board.state[0][0] = 1
        game.board.state[0][1] = 1
        game.board.state[0][2] = 1

        self.assertTrue(game.is_game_terminated())


if __name__ == '__main__':
    unittest.main()
