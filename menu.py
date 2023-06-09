import os
import open_file
from game import *
from tkinter import *
from tkinter import ttk
from const import *


def generate_standard_buttons(root=Root):
    """This code generates the standard buttons associated with the menu. This
    function is called by the menu generator to generate all of the 'standard'
    buttons for the user. Custom buttons are handled in a different function."""

    game_array = [
        Game(PC98, root),
        Game(TOUHOU6, root),
        Game(TOUHOU7, root),
        Game(TOUHOU75, root),
        Game(TOUHOU8, root),
        Game(TOUHOU9, root),
        Game(TOUHOU95, root),
        Game(TOUHOU10, root),
        Game(TOUHOU11, root),
        Game(TOUHOU12, root),
        Game(TOUHOU123, root),
        Game(TOUHOU125, root),
        Game(TOUHOU128, root),
        Game(TOUHOU13, root),
        Game(TOUHOU135, root),
        Game(TOUHOU14, root),
        Game(TOUHOU143, root),
        Game(TOUHOU145, root),
        Game(TOUHOU15, root),
        Game(TOUHOU155, root),
        Game(TOUHOU16, root),
        Game(TOUHOU165, root),
        Game(TOUHOU17, root),
        Game(TOUHOU175, root),
        Game(TOUHOU18, root),
        Game(TOUHOU185, root),
        Game(TOUHOU19, root),
    ]
    x_off = 20
    y_off = 20
    for x in game_array:
        x.button.place(x=x_off, y=y_off)
        y_off += 20
        if y_off > 900:
            x_off


def generate_custom_buttons(root=Root):
    """This is a feature that might be implemented later. Implmements
    ability to add custom buttons to the interface, complete with button text,
    images, and links. This will be implemented once everything else is.

    Current idea is to take user input, and make a JSON file based on the
    input in order to store user data and eventually load it later. Max of 7
    buttons."""
    pass


def generate_menu():
    """Generates menu from helper functions."""
    root = Root()

    generate_standard_buttons(root)

    root.mainloop()
