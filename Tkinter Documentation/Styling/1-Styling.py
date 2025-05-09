import tkinter as tk
from tkinter import ttk, font

# window
window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

# print(font.families())

# style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('classic')

style.configure('new.TButton', foreground = 'green', font = ('Jokerman', 20))
style.map('new.TButton',
          foreground = [('pressed', 'red'), ('disabled', 'yellow')],
          background = [('pressed', 'green'), ('active', 'blue')])

# widgets
label = ttk.Label(
    window, 
    text = 'A label\nAnd then type on another line',
    background = 'red',
    foreground = 'white',
    font = ('Cooper Black', 20),
    justify = 'right')

label.pack()

button = ttk.Button(window, text = 'A Button', style = 'new.TButton')
button.pack()

# Exercise
style.configure('TFrame', background = 'pink')

frame = ttk.Frame(window, width = 100, height = 200)
frame.pack()

# run
window.mainloop()