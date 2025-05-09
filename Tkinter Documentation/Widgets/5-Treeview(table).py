import tkinter as tk
from tkinter import ttk
import random

# Create The Main Window
window = tk.Tk()
window.geometry("800x600")
window.title("Tables")

# data 
first_names = ['Bob', 'Susan', 'John', 'Gary', 'Jerry', 'Tom']
last_names = ['Smith', 'Brown', 'Mike', "Jack", 'Dave','Tayson']

# treeview
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Last name')
table.heading('email', text = 'Email' )
table.pack()

# Insert Values Into Table
for i in range(10):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first[0]}_{last}@gmail.com"
    data = (first, last, email)
    table.insert(parent = '', index = 0, values = data)

table.insert(parent='', index = tk.END, values = ("xxxxx", 'yyyyyy', 'zzzzzz'))

# Events
def select_item(_):
    for i in table.selection():
        print(table.item(i)['values'])
        print(table.item(i))
        print(table.selection())

def delete_item(_):
   for i in table.selection():
       table.delete(i)

table.bind("<<TreeviewSelect>>", select_item)
table.bind("<Delete>", delete_item)

# Run
window.mainloop()