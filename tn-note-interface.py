from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()  # Initial Tk instance
root.title("Toasty Note")  # Toasty Note window title
root.minsize(width=200, height=200)  # Minimum size requirements for the tn window
mainframe = ttk.Frame(root, padding="12 12 12 12")  # Slight padding edge around the entire frame
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Organizes the GUI into a grid of columns and rows
mainframe.columnconfigure(0, weight=1)  # No fucking idea yet
mainframe.rowconfigure(0, weight=1)  # See above comment
root.option_add('*tearOff', FALSE)  # Thing so that menu-bars can't be made into their own awkward windows

quit_button = ttk.Button(mainframe, text='Quit', command=root.quit).grid(column=1, row=0)  # Cute lil quit button!
note_text_window = Text(mainframe, width=60, height=30).grid(column=0, row=0)  # Text window to type shit into
root.mainloop()  # Run this bitch
