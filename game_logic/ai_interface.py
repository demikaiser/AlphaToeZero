# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import _thread
import unittest

from game_agent_search import ai_search_minimax
from game_agent_learning import ai_search_alpha_zero

class AIInterface(object):
    """ AI interface class that connects the main gui to AI agents.

    In order to add more AI search/learning methods, there are three things
    to make changes.

    First, make files for the AI method under either game_agent_learning or
    game_agent_search folder. Put files when you see relevant, or you can make
    a new folder to keep the files.

    Second, the new AI method should be added to GUI panel to enable users to
    select the new one. Go to the main_gui.py file, search for "list_agents".
    Simply add the name of the method at the end of the list. It will appear
    on the GUI panel.

    Lastly, come back to this file and add the interface of the new method
    under the if-else ladder under the function "generate_next_move". The
    function should be started as a new thread to make GUI function during
    the searching time.
    """

    def __init__(self, context_gui, context_game,
                 side, current_state, method):
        self.context_gui = context_gui
        self.context_game = context_game
        self.player_side = side
        self.init_state = current_state
        self.method = method

    def generate_next_move(self):

        try:
            if "Minimax" in self.method:
                _thread.start_new_thread(ai_search_minimax.make_move,
                                         (self.context_gui,
                                          self.context_game,
                                          self.player_side,
                                          self.init_state, ))
            elif "AlphaZero" in self.method:
                _thread.start_new_thread(ai_search_alpha_zero.make_move,
                                         (self.context_gui,
                                          self.context_game,
                                          self.player_side,
                                          self.init_state,))
            elif "SOMETHING ELSE" in self.method:
                pass



        except:
            print("Thread error in AI Interface.")


class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        print('Unit Test 0000 Executed!')


if __name__ == '__main__':
    unittest.main()