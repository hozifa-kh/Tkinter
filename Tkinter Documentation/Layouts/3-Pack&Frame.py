import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Pack with Frames')
window.geometry('400x600')

# Top Frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'Label1', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label2', background = 'blue')

# Middle Widget
label3 = ttk.Label(window, text = 'Label 3', background = 'green')

# Bottom Frame
bottom_frame = ttk.Frame(window)
button = ttk.Button(bottom_frame, text = 'A Button')
label4 = ttk.Label(bottom_frame, text = 'last of the labels', background = 'orange' )
button2 = ttk.Button(bottom_frame, text ='Another Button')

# Exercise Frame Inside Bottom Frame
exercise_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(exercise_frame, text = 'Button 3')
button4 = ttk.Button(exercise_frame, text = 'Button 4')
button5 = ttk.Button(exercise_frame, text = 'Button 5')

# Top Layout
label1.pack(expand = True, fill = 'both')
label2.pack(expand = True, fill = 'both')
top_frame.pack(expand = True, fill = 'both')

# Middle Layout
label3.pack(expand = True)

# Bottom Layout
button.pack(side = 'left', expand = True, fill = 'both')
label4.pack(side = 'left', expand = True, fill = 'both')
button2.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

# Exercise Frame Layout
button3.pack(expand = True, fill = 'both')
button4.pack(expand = True, fill = 'both')
button5.pack(expand = True, fill = 'both')
exercise_frame.pack(side = 'left', expand = True, fill = 'both')

# Run
window.mainloop()