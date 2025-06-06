import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# Window
window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("300x150")

# Title Label
title_label = ttk.Label(master = window, text = "Miles To Kilometers", font = "Calibri 24 bold")
title_label.pack()

# Input Field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side="left", padx = 10)
button.pack(side="left")
input_frame.pack(pady = 5)

# Output field
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = "Output",
    font = "Calibri 24",
    textvariable = output_string
)
output_label.pack(pady = 5)

# Run
window.mainloop()