import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry("600x400")
window.title("Menu")

# Menu
menu = tk.Menu(window)

# Sub Menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = "New", command = lambda: print("New File"))
file_menu.add_separator()
file_menu.add_command(label = "Open", command = lambda: print("Open File"))
menu.add_cascade(label = "File", menu = file_menu)

# Another Sub Menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Help Entry', command = window.quit)

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = "check", onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label = "Help", menu = help_menu)

# Exercise
exercise_menu = tk.Menu(menu, tearoff = 0)
exercise_sub_menu = tk.Menu(menu, tearoff = 0)

exercise_sub_menu.add_command(label = "color", command = lambda: print("Color"))
exercise_sub_menu.add_radiobutton(label = 'color bool')

exercise_menu.add_cascade(label = 'Sub Menu', menu = exercise_sub_menu)
menu.add_cascade(label = 'Menu 3', menu = exercise_menu)

window.configure(menu = menu)

# Menu Button
menu_button = ttk.Menubutton(window, text = "Menu Button")
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff = False)
button_sub_menu.add_command(label = 'entry 1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label = 'check 1')
# menu_button.configure(menu = menu_button)
menu_button['menu'] = button_sub_menu

# Run
window.mainloop()