import tkinter as tk
from tkinter import ttk

# Set Window
window = tk.Tk()
window.geometry("800x500")

# Set Check Button
check_bool_var = tk.BooleanVar()
check1 = ttk.Checkbutton(
    window,
    text = "checkbox 1",
    command = lambda: print(radio_var.get()),
    variable = check_bool_var ,
)
check1.pack()

# Set Radio Buttons
def radio_func():
    print(check_bool_var.get())
    check_bool_var.set(False)
    

radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'RadioButton 1',
    value = "A",
    variable = radio_var,
    command = radio_func
)
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text = 'RadioButton 2',
    value = "B",
    variable = radio_var,
    command = radio_func
)
radio2.pack()

# Run
window.mainloop()
