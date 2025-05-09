import tkinter as tk
from tkinter import ttk

# Create The Main Window
window = tk.Tk()
window.geometry("600x400")
window.title("Frames & Parenting")

# Frame
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')

# master setting
label = ttk.Label(frame, text = "Label in frame")
label.pack()

button = ttk.Button(frame, text = 'Button in frame')
button.pack()

# example
label2 = ttk.Label(window, text = 'Label Outside frame')
label2.pack(side = 'left')

# Exercise
exercise_frame = ttk.Frame(window, width = 200, height = 200, relief = tk.GROOVE)
exercise_frame.pack_propagate(False)
exercise_frame.pack(side = 'left')

exercise_label = ttk.Label(exercise_frame, text = 'Exercise Label in Frame')
exercise_label.pack()

exercise_button = ttk.Button(exercise_frame, text = 'Exercise Button in Frame')
exercise_button.pack()

exercise_entry = ttk.Entry(exercise_frame)
exercise_entry.pack()

# Run
window.mainloop()