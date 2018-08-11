# Copyright (C) Jake Jonghun Choi - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Written by Jake Jonghun Choi <demikaiser13@gmail.com>

import tkinter
import unittest


class MainGui(tkinter.Frame):
    """
    Main GUI window that contains all.
    """

    @staticmethod
    def start():
        MainGui.root = tkinter.Tk()
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
        self.init_console_frame()

    def init_master_frame(self):
        """
        Creates the master frame.
        """
        self.masterFrame = tkinter.Frame(MainGui.root, bg="black")
        self.masterFrame.pack(fill=tkinter.BOTH, expand=1)

    def init_slave_frame(self):
        """
        Creates the slave frame that contains the game and option frames.
        """
        self.slaveFrame = tkinter.Frame(self.masterFrame, bg="cyan",
                                         width=1000, height=400)
        self.slaveFrame.pack(fill=tkinter.BOTH, expand=1)

    def init_menus(self):
        """
        Creates a menu bar and the menus inside.
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
        """
        Creates the master frame.
        """
        self.bottomFrame = tkinter.Frame(self.slaveFrame, bg="red",
                                         width=400, height=400)
        self.bottomFrame.pack(side=tkinter.LEFT)

    def init_option_frame(self):
        """
        Creates the option frame.
        """
        self.optionFrame = tkinter.Frame(self.slaveFrame, bg="yellow",
                                         width=600, height=400)
        self.optionFrame.pack(side=tkinter.RIGHT)

    def init_console_frame(self):
        """
        Creates the console frame.
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

    def function_console_print(self, message):
        """
        Prints a line of message to the console.

        :param message: Message to print.
        """
        self.console.insert(tkinter.END, message)
        self.console.selection_clear(0, tkinter.END)
        self.console.selection_set("end")
        self.console.see("end")














    def function_exit(self):
        exit()


    def function_hi(self):
        print('Hi!')






class UnitTest(unittest.TestCase):
    """
    Unit tests for TDD process.
    """

    def test_case_0(self):
        print('Unit Test 0 Executed!')

if __name__ == '__main__':
    unittest.main()