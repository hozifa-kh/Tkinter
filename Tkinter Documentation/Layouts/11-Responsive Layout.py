import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, start_size):

        # setup main window
        super().__init__()
        self.title("Responsive layout")
        self.geometry(f'{start_size[0]}x{start_size[1]}')
        
        # create empty frame
        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = 'both')

        # check size class
        SizeNotifier(self, {
                            600: self.create_medium_layout,
                            300: self.create_small_layout,
                            1200: self.create_large_layout
                            })
        # run
        self.mainloop()

    # layout functions
    def create_small_layout(self):
        self.frame.pack_forget()

        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text = 'Label 1', background = 'red').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        ttk.Label(self.frame, text = 'Label 2', background = 'green').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        ttk.Label(self.frame, text = 'Label 3', background = 'blue').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        ttk.Label(self.frame, text = 'Label 4', background = 'yellow').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        self.frame.pack(expand = True, fill = 'both')

    def create_medium_layout(self):
        self.frame.pack_forget()

        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight = 1, uniform = 'a')
        self.frame.rowconfigure((0,1), weight = 1, uniform = 'a')
        self.frame.pack(expand = True, fill = 'both')

        ttk.Label(self.frame, text = 'Label 1', background = 'red').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 2', background = 'green').grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 3', background = 'blue').grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 4', background = 'yellow').grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 10)

    def create_large_layout(self):
        self.frame.pack_forget()

        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.frame.rowconfigure(0, weight = 1, uniform = 'a')
        self.frame.pack(expand = True, fill = 'both')

        ttk.Label(self.frame, text = 'Label 1', background = 'red').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady =10) 
        ttk.Label(self.frame, text = 'Label 2', background = 'green').grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 3', background = 'blue').grid(row = 0, column = 2, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 4', background = 'yellow').grid(row = 0, column = 3, sticky = 'nsew', padx = 10, pady = 10)

class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None
        
        # check resizing event
        self.window.bind('<Configure>', self.check_size)

        # update window 
        self.window.update()

        # set min size for window
        min_width = list(self.size_dict)[0]
        min_height = self.window.winfo_height()
        self.window.minsize(min_width, min_height)

        
    # check current size function
    def check_size(self, event):
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

            for min_size in self.size_dict:
                delta = window_width - min_size
                if delta >= 0:
                    checked_size = min_size
            
            if checked_size != self.current_min_size:
                self.current_min_size = checked_size
                self.size_dict[self.current_min_size]()
        
app = App((400,300))