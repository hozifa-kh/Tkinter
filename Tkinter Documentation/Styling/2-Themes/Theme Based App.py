import tkinter as tk
from tkinter import ttk
import os

class App(tk.Tk):
    def __init__(self, title, size):
       
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0],size[1])

        # theme
        current_folder = os.path.dirname(os.path.abspath(__file__))
        self.tk.call('source', rf'{current_folder}\Azure\azure.tcl')
        self.tk.call('set_theme', 'dark')
        print(dir(self.tk.call))

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)

        self.create_widgets()

    def create_widgets(self):

        # create the widgets
        menu_button1 = ttk.Button(self, text = 'Button 1')
        menu_button2 = ttk.Button(self, text = 'Button 2')
        menu_button3 = ttk.Button(self, text = 'Button 3')

        menu_slider1 = ttk.Scale(self, orient = 'vertical')
        menu_slider2 = ttk.Scale(self, orient = 'vertical')

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text = 'Check 1')
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'Check 2')

        entry = ttk.Entry(self)

        # create the grid
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        # place the widgets
        menu_button1.grid(row = 0, column = 0, sticky = 'nsew', columnspan = 2, padx = 4, pady = 4)
        menu_button2.grid(row = 0, column = 2, sticky = 'nsew', padx = 4, pady = 4)
        menu_button3.grid(row = 1, column = 0, sticky = 'nsew', columnspan = 3, padx = 4, pady = 4)

        menu_slider1.grid(row = 2, column = 0, rowspan = 2, sticky = 'ns', pady = 20)
        menu_slider2.grid(row = 2, column = 2, rowspan = 2, sticky = 'ns', pady = 20)

        # toggle layout
        toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = 'nsew')
        menu_toggle1.pack(side = 'left', expand = True)
        menu_toggle2.pack(side = 'left', expand = True)

        # entry layout
        entry.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = 'center')

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
        
        # main widgets
        Frame(self, 'Label 1', 'Button 1', 'red')
        Frame(self, 'Label 2', 'Button 2', 'blue')
        
class Frame(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)
        self.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        
        # frame widgets
        label = ttk.Label(self, text = label_text, background = label_background)
        button = ttk.Button(self, text = button_text)

        # widgets layout
        label.pack(expand = True, fill = 'both')
        button.pack(expand = True, fill = 'both', pady = 10)

App("Theme Based App", (600,600)) 
