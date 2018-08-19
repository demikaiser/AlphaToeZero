# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import random
import time
import _thread
import unittest

from game_agent_search import ai_search_minimax
from game_agent_learning import ai_search_alpha_zero

class AIInterface(object):
    """ AI interface class that connects the main gui to AI agents.
    """

    def __init__(self, context_gui, context_game, side, current_state):
        self.context_gui = context_gui
        self.context_game = context_game
        self.player_side = side
        self.init_state = current_state
        pass

    def generate_next_move(self):
        try:
            _thread.start_new_thread(ai_search_minimax.make_move,
                                     (self.context_gui,
                                        self.context_game,
                                        self.player_side,
                                        self.init_state, ))
        except:
            print("Thread error in AI Interface.")


class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        print('Unit Test 0000 Executed!')


if __name__ == '__main__':
    unittest.main()