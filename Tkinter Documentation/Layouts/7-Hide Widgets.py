import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Hide Widgets")
window.geometry("600x400")

# Place
# def toggle_label_place():
#     global label_visible 

#     if label_visible:
#         label.place_forget()
#         label_visible = False
#     else:
#         label_visible = True
#         label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        
# button = ttk.Button(window, text = 'toggle Label', command = toggle_label_place)
# button.place(x = 10, y = 10)

# label_visible = True
# label = ttk.Label(window, text = 'A Label')
# label.place(relx = 0.5, rely = 0.5, anchor = 'center')

# Grid
# def toggle_label_grid():
#     global label_visible
    
#     if label_visible:
#         label.grid_forget()
#         label_visible = False
#     else:
#         label_visible = True
#         label.grid(row = 0, column = 1)

# window.columnconfigure((0,1), weight = 1, uniform = 'a')
# window.rowconfigure(0, weight = 1, uniform = 'a')

# button = ttk.Button(window, text = 'toggle Label', command = toggle_label_grid)
# button.grid(row = 0, column = 0)

# label_visible = True
# label = ttk.Label(window, text = 'A Label')
# label.grid(row = 0, column = 1)

# Pack
def toggle_label_pack():
    global label_visible

    if label_visible:
        label.pack_forget()
        frame.pack(expand = True, before = button)
        label_visible = False
    else:
        frame.pack_forget()
        label.pack(expand = True, before = button)
        label_visible = True

label_visible = True
label = ttk.Label(window, text = 'A Label')
label.pack(expand = True)

button = ttk.Button(window, text = 'toggle Label', command = toggle_label_pack)
button.pack()

frame = ttk.Frame(window)

# Run
window.mainloop()