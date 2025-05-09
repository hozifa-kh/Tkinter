import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("More on the window")
# window.geometry("600x400+0+0")
# window.iconbitmap(r'C:\Users\Hp\Desktop\Tkinter practice\pythonlogo.ico')

# Exercise
window_width = 600
window_height = 400
display_width = window.winfo_screenwidth() # Your Screen (Moniter) Width
display_height = window.winfo_screenheight() # Your Screen Height

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{left}+{top}")

# Window Sizes
window.minsize(200,100)
# window.maxsize(800,900)
# window.resizable(False, True)

# Screen Attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Window Attributes
window.attributes('-alpha', 1)  # Transparency
# window.attributes('-topmost', True) # Always Stay on top of other apps
# window.attributes('-disabled', True) # Disable the Window
# window.attributes('-fullscreen', True) # Make App Full Screen

# Security Event
window.bind("<Escape>", lambda event: window.quit())

# Title Bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1, rely = 1, anchor = 'se')

# Run
window.mainloop()