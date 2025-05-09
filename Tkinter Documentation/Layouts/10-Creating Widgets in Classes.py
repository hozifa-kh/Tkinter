import tkinter as tk
from tkinter import ttk

def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(parent)

    # grid layout
    frame.rowconfigure(0, weight = 1, uniform = 'a')
    frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')

    # widgets
    ttk.Label(frame, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
    ttk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')

    return frame.pack(expand = True, fill = 'both', padx = 10, pady = 10)

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, exercise_text):
        super().__init__(master = parent)

        # grid layout
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')

        # widgets
        ttk.Label(self, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
        ttk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')
        self.exercise_entry_field(exercise_text)

        self.pack(expand = True, fill = 'both', padx = 10, pady = 10)
    
    def exercise_entry_field(self, text):

        frame = ttk.Frame(self)
        ttk.Entry(frame).pack(expand = True, fill = 'both')
        ttk.Button(frame, text = text).pack(expand = True, fill = 'both')
        return frame.grid(row = 0, column = 2, sticky = 'nsew')
         
# window
window = tk.Tk()
window.title("Widgets and return")
window.geometry("400x600")

# widgets
# create_segment(window, 'label', 'button').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'test', 'click').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'hello', 'test').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'bye', 'launch')
# create_segment(window, 'last one', 'exit')


Segment(window, 'label', 'button', 'exercise')
Segment(window, 'test', 'click', 'exercise')
Segment(window, 'hello', 'test', 'exercise')
Segment(window, 'bye', 'launch', 'exercise')
Segment(window, 'last one', 'exit', 'exercise')

# run
window.mainloop()