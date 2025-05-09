import customtkinter as ctk

# main window
app = ctk.CTk(fg_color = '#FF00FF')
app.geometry('300x200')

# Drag The Window Functions
def start_move(event):
    global x1, y1

    x1 = event.x
    y1 = event.y

def do_move(event):
    x = event.x_root - x1
    y = event.y_root - y1

    app.geometry(f'+{x}+{y}')

# Remove Title bar
app.overrideredirect(True)

# create custom title bar
title_bar = ctk.CTkFrame(app, height = 32, fg_color="#6200EE", corner_radius = 0)
title_bar.pack(fill = 'x', side = 'top')

title_label = ctk.CTkLabel(title_bar, text = 'My App', text_color = 'white')
title_label.pack(side = 'left', padx = 10)

close_button = ctk.CTkButton(
    title_bar, text = 'X',
    width = 30, height = 28,
    fg_color = "#3700B3", hover_color = "#BB86FC",
    corner_radius = 0, command = app.destroy)
close_button.pack(side = 'right', padx = 2, pady = 2)

# make window draggable
title_bar.bind('<Button-1>', start_move)
title_bar.bind('<B1-Motion>', do_move)

# Toggle Full Screen (Double Click)
def toggle_maximize(event):
    '''Toggle Maximize The Screen When Double Click The Title Bar'''
    global is_maximized
    
    if not is_maximized:
        app.state('zoomed')
        is_maximized = True
    else:
        app.state('normal')
        is_maximized = False

is_maximized = False
title_bar.bind('<Double-Button-1>', toggle_maximize)

# run
app.mainloop()