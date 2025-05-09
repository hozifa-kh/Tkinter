import customtkinter as ctk
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

# main window
app = ctk.CTk(fg_color = '#FF00FF')
app.geometry('300x200')

# change the title bar color          *** WINDOWS 11 ONLY ***
try:
    HWND = windll.user32.GetParent(app.winfo_id())
    title_bar_color = 0x000000FF    # Special Type of Int -> 0x00BBGGRR
    windll.dwmapi.DwmSetWindowAttribute(
        HWND,
        35,
        byref(c_int(title_bar_color)),
        sizeof(c_int)
    )

    windll.dwmapi.DwmSetWindowAttribute(
        HWND,
        36,
        byref(c_int(title_bar_color)),
        sizeof(c_int)
    )
except: # Pass The Code If It Get Error
    pass

# run
app.mainloop()