
# Python Ver:   3.5.1
#
# Author:       Krystle A. Tsuda
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Chile relationships.
#
# Tested OS:    This code was written and tested to work with Windows 11.


from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Be sure to import our modules
# so we can have access to them
import phonebook_gui
import phonebook_func


# Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(height,width)
        self.master.maxsize(500,300)
        # this CenterWindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.configure(bg="#F0F0F0")
        # this protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master


        # load in the GUI widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)

        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
