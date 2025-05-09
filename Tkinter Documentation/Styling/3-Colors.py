# Hexadecimal color values are either 3 or 6 digits long
# Hexadecimal values from 0 To F    -> 0 1 2 3 4 5 6 7 8 9 A B C D E F 
# r = red, g = green, b = blue
# ('#rgb') or ('#rrggbb')

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Colors')
window.geometry('400x400')

# widgets
ttk.Label(window, background = 'red').pack(expand = True, fill = 'both')
ttk.Label(window, background = '#08F').pack(expand = True, fill = 'both')
ttk.Label(window, background = '#49b1d6').pack(expand = True, fill = 'both')

# Exercise (create a Brownish color using hex values)
ttk.Label(window, background = '#a51').pack(expand = True, fill = 'both')

# white, black and grey
ttk.Label(window, background = '#000').pack(expand = True, fill = 'both') # black
ttk.Label(window, background = '#888').pack(expand = True, fill = 'both') # grey
ttk.Label(window, background = '#FFF').pack(expand = True, fill = 'both') # white

# run
window.mainloop()