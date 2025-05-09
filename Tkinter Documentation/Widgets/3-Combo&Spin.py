import tkinter as tk
from tkinter import ttk

# Set Main Window 
window = tk.Tk()
window.geometry("800x500")

# Combobox
items = ("Ice Cream", "Apple", "Tomato")

food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo["values"] = items
# combo.configure(values = items)
combo.pack()

# Events
combo.bind("<<ComboboxSelected>>", lambda event: combo_label.configure(text = f"Selected value: {food_string.get()}"))

combo_label = ttk.Label(window)
combo_label.pack()

# Spinbox

# spin_values = ["A", "B", "C", "D", "E"]
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window,
                   from_ = 3,
                   to = 20,
                   increment = 3,
                   command = lambda : print(spin_int.get()),
                   textvariable = spin_int,
                   )
# spin["values"] = spin_values
spin.bind('<<Increment>>', lambda event: print("up"))
spin.bind('<<Decrement>>', lambda event: print("down"))
spin.pack()


# Run
window.mainloop()