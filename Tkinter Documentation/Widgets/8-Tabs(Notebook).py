import tkinter as tk
from tkinter import ttk

# Create The Main Window
window = tk.Tk()
window.geometry("600x400")
window.title("Tabs")

# Notebook Widget
notebook = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'Label in Tab 1')
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in Tab 1')
button1.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'Label in Tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

# Exercise
tab3 = ttk.Frame(notebook)
button3 = ttk.Button(tab3, text = 'Button in Tab 3')
button3.pack()
button3_2 = ttk.Button(tab3, text = 'Button2 in Tab 3')
button3_2.pack()
label3 = ttk.Label(tab3, text = 'Label in Tab 3')
label3.pack()

notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')
notebook.add(tab3, text = 'Tab 3')
notebook.pack()

# Run
window.mainloop()