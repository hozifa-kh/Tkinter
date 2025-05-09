# Tkinter Bind Events 
# https://www.pythontutorial.net/tkinter/tkinter-event-binding/

# - place.bind("<modifier-type-detail>", function)
# - There Is a Default Parameter for Function

import tkinter as tk
from tkinter import ttk

# Set Main Window
window = tk.Tk()
window.title("Demo")
window.geometry("800x500")

# Set Text
text = tk.Text(window)
text.pack()

# Event
text.bind("<FocusOut>", lambda event: print("Focus Out"))


# Run
window.mainloop()
