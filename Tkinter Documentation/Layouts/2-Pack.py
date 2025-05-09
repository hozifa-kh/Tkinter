# side = 'top' (Default)      expand = 'False' (Default)      fill = 'none' (Default)
# ipadx & ipady -> Extend widget ,  padx & pady -> Add more Space

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Pack")
window.geometry("400x600")

# Widgets
label1 = ttk.Label(window, text = "Label 1", background = 'red')
label2 = ttk.Label(window, text = "Label 2", background = 'blue')
label3 = ttk.Label(window, text = "Label 3", background = 'green')
button = ttk.Button(window, text = "Button")

# Exercise      
label1.pack(side = 'top', expand = True, fill = 'both', pady = 10, padx = 10)   
label2.pack(side = 'left', expand = True, fill = 'both')                        
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', expand = True, fill = 'both')

# Run
window.mainloop()