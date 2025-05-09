# Widgets Are Placed On Top Of Other Widgets When They Are Created (Not When They Are Placed)
# widget.lift() & widget.tkraise()  -> Raise The Widget On Top Of Other Widgets
# widget.lift(aboveThis = widget2)  -> Raise The Widget On Top Of Widget2 (widget.tkraise() also)
# widget.lower()                    -> Lower The Widget Behind Other Widgets

import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Stacking Order")
window.geometry("400x400")

# Widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'green')
label2 = ttk.Label(window, text = 'Label 2', background = 'red')
label3 = ttk.Label(window, text = 'Label 3', background = 'blue')

button1 = ttk.Button(window, text = 'Raise Label 1', command = lambda: label1.tkraise(aboveThis = label2))
button2 = ttk.Button(window, text = 'Raise Label 2', command = lambda: label2.tkraise())
button3 = ttk.Button(window, text = 'Raise Label 3', command = lambda: label3.tkraise())

# Layout
label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place(x = 150, y = 60, width = 140, height = 100)
label3.place(x = 100, y = 50, width = 100, height = 150)

button1.place(rely = 1, relx = 0.8, anchor = 'se')
button2.place(rely = 1, relx = 1, anchor = 'se')
button3.place(rely = 1, relx = 0.6, anchor = 'se')

# Run
window.mainloop()