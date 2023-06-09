import os
import open_file
from tkinter import *
from tkinter import ttk
from const import *


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("TouhouLauncherV2")
        self.minsize(1080, 1080)


class Game:
    def __init__(
        self,
        name,
        root=Root,
        dir="",
    ):
        self.name = name
        self.dir = dir
        self.root = root
        self.button = Button(root, text=name)
