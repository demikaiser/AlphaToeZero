# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import tkinter
import unittest
import os

import config
from game_logic import tic_tac_toe

class MainGui(tkinter.Frame):
    """Main GUI window that contains all main components.
    """

    root = tkinter.Tk()

    @staticmethod
    def start():
        """Starts the GUI application.
        """
        MainGui.root.title("AlphaToeZero")
        MainGui.root.resizable(width=False, height=False)
        MainGui.root.geometry("1000x600")

        # Promote the object to the static variable for the remote access.
        MainGui.instance = MainGui()
        MainGui.root.mainloop()

    def __init__(self):
        self.init_master_frame()
        self.init_slave_frame()
        self.init_menus()
        self.init_game_frame()
        self.init_option_frame()
        self.init_sub_option_frames()
        self.init_sub_option_frame_0_widgets()
        self.init_sub_option_frame_1_widgets()
        self.init_sub_option_frame_2_widgets()
        self.init_console_frame()
        self.init_game_images()
        self.init_game_buttons()
        self.set_game_button_base_images()

        # Disable the stop button since nothing has been started.
        self.buttonGameStop.configure(state=tkinter.DISABLED)

        # Disable all game button tiles.
        self.disable_all_buttonGameTiles()

    def init_master_frame(self):
        """Creates the master frame.
        """
        self.masterFrame = tkinter.Frame(MainGui.root, bg="black")
        self.masterFrame.pack(fill=tkinter.BOTH, expand=1)

    def init_slave_frame(self):
        """Creates the slave frame that contains the game and option frames.
        """
        self.slaveFrame = tkinter.Frame(self.masterFrame, bg="cyan",
                                        width=1000, height=400)
        self.slaveFrame.pack(fill=tkinter.BOTH, expand=1)

    def init_menus(self):
        """Creates a menu bar and the menus inside.
        """
        menu = tkinter.Menu(self.masterFrame)
        MainGui.root.config(menu=menu)

        file = tkinter.Menu(menu)
        file.add_command(label="Exit", command=self.function_exit)
        menu.add_cascade(label="File", menu=file)

        edit = tkinter.Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

    def init_game_frame(self):
        """Creates the master frame.
        """
        self.gameFrame = tkinter.Frame(self.slaveFrame, bg="red",
                                       width=400, height=400)
        self.gameFrame.pack(side=tkinter.LEFT)

        self.gameInnerFrame = tkinter.Frame(self.gameFrame, bg="white",
                                            width=300, height=300)
        self.gameInnerFrame.pack(fill="both", expand=True, padx=50, pady=50)

    def init_option_frame(self):
        """Creates the option frame.
        """
        self.optionFrame = tkinter.Frame(self.slaveFrame, bg="yellow",
                                         width=600, height=400)
        self.optionFrame.pack(side=tkinter.RIGHT)

    def init_sub_option_frames(self):
        """Creates all sub-option frames to contain widgets.
        """

        self.subOptionFrame0 = tkinter.Frame(self.optionFrame, bg="green",
                                             width=200, height=400)

        self.subOptionFrame0.pack(side=tkinter.LEFT)

        self.subOptionInnerFrame0 = tkinter.Frame(self.subOptionFrame0,
                                                  bg="white",
                                                  width=150, height=350,
                                                  relief=tkinter.RAISED,
                                                  borderwidth=1)
        self.subOptionInnerFrame0.pack(fill=tkinter.BOTH, expand=True,
                                       padx=25, pady=25)

        self.subOptionFrame1 = tkinter.Frame(self.optionFrame, bg="cyan",
                                             width=200, height=400)
        self.subOptionFrame1.pack(side=tkinter.LEFT)

        self.subOptionInnerFrame1 = tkinter.Frame(self.subOptionFrame1,
                                                  bg="white",
                                                  width=150, height=350,
                                                  relief=tkinter.RAISED,
                                                  borderwidth=1)
        self.subOptionInnerFrame1.pack(fill=tkinter.BOTH, expand=True,
                                       padx=25, pady=25)

        self.subOptionFrame2 = tkinter.Frame(self.optionFrame, bg="magenta",
                                             width=200, height=400)
        self.subOptionFrame2.pack(side=tkinter.LEFT)

        self.subOptionInnerFrame2 = tkinter.Frame(self.subOptionFrame2,
                                                  bg="white",
                                                  width=150, height=350,
                                                  relief=tkinter.RAISED,
                                                  borderwidth=1)
        self.subOptionInnerFrame2.pack(fill=tkinter.BOTH, expand=True,
                                       padx=25, pady=25)

    def init_sub_option_frame_0_widgets(self):
        """Creates widgets for sub-option frame 0.
        """

        # Possible Agent Selections.
        agents = [
            ("Human", "Human"),
            ("AI with Search", "AI with Search"),
            ("AI with Learning", "AI with Learning")
        ]

        self.labelOPlayerSelection = tkinter.Label(self.subOptionInnerFrame0,
                                                   text="O Player Selection")
        self.labelOPlayerSelection.pack(fill=tkinter.X, padx=6, pady=3)

        self.variable_o_player_selection = tkinter.StringVar()
        self.variable_o_player_selection.set("Human")

        for text, mode in agents:
            b = tkinter.Radiobutton(self.subOptionInnerFrame0, text=text,
                                    variable=self.variable_o_player_selection,
                                    value=mode)
            b.pack(anchor=tkinter.W)

        self.labelXPlayerSelection = tkinter.Label(self.subOptionInnerFrame0,
                                                   text="X Player Selection")
        self.labelXPlayerSelection.pack(fill=tkinter.X, padx=6, pady=3)

        self.variable_x_player_selection = tkinter.StringVar()
        self.variable_x_player_selection.set("Human")

        for text, mode in agents:
            b = tkinter.Radiobutton(self.subOptionInnerFrame0, text=text,
                                    variable=self.variable_x_player_selection,
                                    value=mode)
            b.pack(anchor=tkinter.W)

        self.variableOption0 = tkinter.IntVar()
        tkinter.Checkbutton(self.subOptionInnerFrame0,
                            text="Option 0",
                            variable=self.variableOption0)\
            .pack(anchor=tkinter.W)


        self.variableOption1 = tkinter.IntVar()
        tkinter.Checkbutton(self.subOptionInnerFrame0,
                            text="Option 1",
                            variable=self.variableOption1)\
            .pack(anchor=tkinter.W)

        self.variableOption2 = tkinter.IntVar()
        tkinter.Checkbutton(self.subOptionInnerFrame0,
                            text="Option 2",
                            variable=self.variableOption2)\
            .pack(anchor=tkinter.W)

        self.buttonGameStart = tkinter.Button(self.subOptionInnerFrame0,
                                              text="Start",
                                              command=self.function_game_start)
        self.buttonGameStart.pack(fill=tkinter.X, padx=6, pady=3)

        self.buttonGameStop = tkinter.Button(self.subOptionInnerFrame0,
                                             text="Stop",
                                             command=self.function_game_stop)
        self.buttonGameStop.pack(fill=tkinter.X, padx=6, pady=3)

        # Expand the frame to the original size after packing.
        self.subOptionFrame0.pack_propagate(0)

    def init_sub_option_frame_1_widgets(self):
        """Creates widgets for sub-option frame 1.
        """







        # Expand the frame to the original size after packing.
        self.subOptionFrame1.pack_propagate(0)

    def init_sub_option_frame_2_widgets(self):
        """Creates widgets for sub-option frame 2.
        """








        # Expand the frame to the original size after packing.
        self.subOptionFrame2.pack_propagate(0)

    def init_console_frame(self):
        """Creates the console frame.
        """
        self.consoleFrame = tkinter.Frame(self.masterFrame, bg="blue",
                                          width=1000, height=400)
        self.consoleFrame.pack(side=tkinter.TOP)

        # Set up the scroll bar and scroll view.
        scrollbar = tkinter.Scrollbar(self.consoleFrame)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        self.console = tkinter.Listbox(self.consoleFrame,
                                       width=1000, height=400,
                                       yscrollcommand=scrollbar.set)

        self.console.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        scrollbar.config(command=self.console.yview)

    def init_game_images(self):
        """Loads all images associated to the game play.
        """
        self.imageEmpty = tkinter.PhotoImage(
            file=os.path.join(config.ASSETS_DIR, "marble_empty.gif")
        )
        self.imageO = tkinter.PhotoImage(
            file=os.path.join(config.ASSETS_DIR, "marble_o.gif")
        )
        self.imageX = tkinter.PhotoImage(
            file=os.path.join(config.ASSETS_DIR, "marble_x.gif")
        )

    def init_game_buttons(self):
        """Creates 9 buttons for the game panel.
        """

        # Game Tile Button 00
        self.buttonGameTile00 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile00)
        self.buttonGameTile00.place(x=0, y=0)

        # Game Tile Button 01
        self.buttonGameTile01 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile01)
        self.buttonGameTile01.place(x=100, y=0)

        # Game Tile Button 02
        self.buttonGameTile02 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile02)
        self.buttonGameTile02.place(x=200, y=0)

        # Game Tile Button 10
        self.buttonGameTile10 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile10)
        self.buttonGameTile10.place(x=0, y=100)

        # Game Tile Button 11
        self.buttonGameTile11 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile11)
        self.buttonGameTile11.place(x=100, y=100)

        # Game Tile Button 12
        self.buttonGameTile12 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile12)
        self.buttonGameTile12.place(x=200, y=100)

        # Game Tile Button 20
        self.buttonGameTile20 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile20)
        self.buttonGameTile20.place(x=0, y=200)

        # Game Tile Button 21
        self.buttonGameTile21 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile21)
        self.buttonGameTile21.place(x=100, y=200)

        # Game Tile Button 22
        self.buttonGameTile22 = tkinter.Button(self.gameInnerFrame,
                                               command=self.function_buttonGameTile22)
        self.buttonGameTile22.place(x=200, y=200)


    def set_game_button_base_images(self):
        """Sets the base image (empty one) to all buttons for game reset.
        """

        self.buttonGameTile00.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile00.image = self.imageEmpty

        self.buttonGameTile01.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile01.image = self.imageEmpty

        self.buttonGameTile02.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile02.image = self.imageEmpty

        self.buttonGameTile10.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile10.image = self.imageEmpty

        self.buttonGameTile11.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile11.image = self.imageEmpty

        self.buttonGameTile12.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile12.image = self.imageEmpty

        self.buttonGameTile20.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile20.image = self.imageEmpty

        self.buttonGameTile21.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile21.image = self.imageEmpty

        self.buttonGameTile22.config(image=self.imageEmpty,
                                     width="100", height="100")
        self.buttonGameTile22.image = self.imageEmpty

    def enable_all_buttonGameTiles(self):
        """ Enables all game tile buttons.
        """

        self.buttonGameTile00.configure(state=tkinter.NORMAL)
        self.buttonGameTile01.configure(state=tkinter.NORMAL)
        self.buttonGameTile02.configure(state=tkinter.NORMAL)
        self.buttonGameTile10.configure(state=tkinter.NORMAL)
        self.buttonGameTile11.configure(state=tkinter.NORMAL)
        self.buttonGameTile12.configure(state=tkinter.NORMAL)
        self.buttonGameTile20.configure(state=tkinter.NORMAL)
        self.buttonGameTile21.configure(state=tkinter.NORMAL)
        self.buttonGameTile22.configure(state=tkinter.NORMAL)

    def disable_all_buttonGameTiles(self):
        """ Disables all game tile buttons.
        """

        self.buttonGameTile00.configure(state=tkinter.DISABLED)
        self.buttonGameTile01.configure(state=tkinter.DISABLED)
        self.buttonGameTile02.configure(state=tkinter.DISABLED)
        self.buttonGameTile10.configure(state=tkinter.DISABLED)
        self.buttonGameTile11.configure(state=tkinter.DISABLED)
        self.buttonGameTile12.configure(state=tkinter.DISABLED)
        self.buttonGameTile20.configure(state=tkinter.DISABLED)
        self.buttonGameTile21.configure(state=tkinter.DISABLED)
        self.buttonGameTile22.configure(state=tkinter.DISABLED)

    def function_buttonGameTile00(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 0, 0
        )

    def function_buttonGameTile01(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 0, 1
        )

    def function_buttonGameTile02(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 0, 2
        )

    def function_buttonGameTile10(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 1, 0
        )

    def function_buttonGameTile11(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 1, 1
        )

    def function_buttonGameTile12(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 1, 2
        )

    def function_buttonGameTile20(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 2, 0
        )

    def function_buttonGameTile21(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 2, 1
        )

    def function_buttonGameTile22(self):
        """ Passes the button input from the user to the game object.
        """

        self.tictactoe_game.make_movement_by_human(
            self.tictactoe_game.turn, 2, 2
        )

    def update_buttonGameTiles(self):
        """ Updates images on the game tile buttons.
        """

        self.update_buttonGameTile(self.buttonGameTile00, 0, 0)
        self.update_buttonGameTile(self.buttonGameTile01, 0, 1)
        self.update_buttonGameTile(self.buttonGameTile02, 0, 2)
        self.update_buttonGameTile(self.buttonGameTile10, 1, 0)
        self.update_buttonGameTile(self.buttonGameTile11, 1, 1)
        self.update_buttonGameTile(self.buttonGameTile12, 1, 2)
        self.update_buttonGameTile(self.buttonGameTile20, 2, 0)
        self.update_buttonGameTile(self.buttonGameTile21, 2, 1)
        self.update_buttonGameTile(self.buttonGameTile22, 2, 2)

    def update_buttonGameTile(self, buttonGameTile, row, col):
        """ Updates individual image on a game tile button.

        Args:
            buttonGameTile: The button tile reference to make a change.
            row: Row number of the movement.
            col: Column number of the movement.

        """

        if self.tictactoe_game.board.state[row][col] == 0:
            buttonGameTile.config(image=self.imageEmpty,
                                         width="100", height="100")
            buttonGameTile.image = self.imageEmpty
        elif self.tictactoe_game.board.state[row][col] == 1:
            buttonGameTile.config(image=self.imageO,
                                  width="100", height="100")
            buttonGameTile.image = self.imageO
        elif self.tictactoe_game.board.state[row][col] == -1:
            buttonGameTile.config(image=self.imageX,
                                  width="100", height="100")
            buttonGameTile.image = self.imageX

    def terminate_game(self, winner):
        """ Terminates the game from the GUI side.

        Args:
            winner: The winner of the game, 0 if draw.
        """

        if winner == 1:
            self.function_console_print("Player O won!")
        elif winner == -1:
            self.function_console_print("Player X won!")
        elif winner == 0:
            self.function_console_print("Draw!")

        # Stop the game.
        self.function_game_stop()

    def function_game_start(self):
        """ Starts a new game.
        """

        self.function_console_print("Game started.")

        player_o_selection = self.variable_o_player_selection.get()
        player_x_selection = self.variable_x_player_selection.get()

        self.tictactoe_game = tic_tac_toe.TicTacToe(player_o_selection,
                                                    player_x_selection,
                                                    self)
        self.tictactoe_game.start_thinking_player_o()

        # Restrict start and stop buttons.
        self.buttonGameStart.configure(state=tkinter.DISABLED)
        self.buttonGameStop.configure(state=tkinter.NORMAL)

        self.enable_all_buttonGameTiles()

    def function_game_stop(self):
        """ Stops the current game and reset everything.
        """

        self.function_console_print("Game stopped.")

        # Restrict start and stop buttons.
        self.buttonGameStart.configure(state=tkinter.NORMAL)
        self.buttonGameStop.configure(state=tkinter.DISABLED)

        self.disable_all_buttonGameTiles()

    def function_console_print(self, message):
        """Prints a line of message to the console.

        Args:
            message: Message to print.
        """
        self.console.insert(tkinter.END, message)
        self.console.selection_clear(0, tkinter.END)
        self.console.selection_set("end")
        self.console.see("end")

    def function_exit(self):
        """Exits the entire program and close the GUI front-end application.
        """
        exit()


class UnitTest(unittest.TestCase):
    """Unit tests for TDD process.
    """

    def test_case_0000(self):
        print('Unit Test 0000 Executed!')

if __name__ == '__main__':
    unittest.main()