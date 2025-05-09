import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create The Main Window
window = tk.Tk()
window.geometry("500x500")
window.title("Sliders")

# Scale
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(
    window,
    command = lambda value: print(scale_float.get()), 
    from_ = 0, 
    to = 25,
    length = 300,
    orient = 'horizontal',
    variable = scale_float)
scale.pack()

# Progress
progress = ttk.Progressbar(
    window,
    variable = scale_float,
    maximum = 25,
    orient = 'horizontal',
    mode = 'indeterminate',
    length = 400,  )
progress.pack()
# progress.start(1000)

# Scrolled Text
scrolled_text = scrolledtext.ScrolledText(window, width = 50, height = 5)
scrolled_text.pack()

# Exercise
prog_int = tk.IntVar()
exercise_prog = ttk.Progressbar(window, variable = prog_int, orient = 'vertical')
exercise_prog.pack()
exercise_prog.start()

label = ttk.Label(window, textvariable = prog_int)
label.pack()

exercise_scale = ttk.Scale(window, variable = prog_int, from_ = 0, to = 100 )
exercise_scale.pack()

# Run
window.mainloop()