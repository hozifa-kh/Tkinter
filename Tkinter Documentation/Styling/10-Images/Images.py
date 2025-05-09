import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os

# Make This Dir The CWD
os.chdir(r'C:\Users\Hp\Desktop\Tkinter\Tkinter Documentation\Styling\images')

def stretch_image(event):
    '''Stretch the image to fill the entire canvas.
    This may result in a distorted image'''

    global resized_tk

    # size
    width = event.width
    height = event.height

    # create an image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on the canvas
    canvas.create_image(0,0, image = resized_tk, anchor = 'nw')

def fill_image(event):
    '''Resize the image to fill the entire canvas while preserving aspect ratio. 
        This may crop parts of the image to ensure no empty space is visible.'''

    global resized_tk

    # current ratio                                     
    canvas_ratio = event.width / event.height       # r = w/h    

    # get coordinates
    if canvas_ratio > image_ratio:    # canvas is wider than the image
        width = int(event.width)
        height = int(width / image_ratio)                                      
    else:  # canvas is narrower than the image                              
        height = int(event.height)                                     
        width = int(height * image_ratio)      

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event.width / 2),
        int(event.height / 2),
        anchor = 'center',
        image = resized_tk)

def show_full_image(event):
    '''Display the full image scaled to fit inside the canvas while keeping aspect ratio.'''
   
    global resized_tk

    # canvas ratio
    canvas_ratio = event.width / event.height

    # get coordinates
    if canvas_ratio > image_ratio:  # canvas is wider than the image
        height= int(event.height)
        width = int(height * image_ratio)
    else:  # canvas in narrower or taller than the image
        width = int(event.width)
        height = int(width / image_ratio)
    
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event.width / 2),
        int(event.height / 2),
        anchor = 'center',
        image = resized_tk)
    
# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# grid layout
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1)

# import an image
image_original = Image.open('raccoon.jpg')
image_ratio = image_original.size[0] / image_original.size[1]   # width / height
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('python_dark.png').resize((30,30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

img_ctk = ctk.CTkImage(
    light_image = Image.open('python_dark.png'),
    dark_image = Image.open('python_light.png'))

# widgets
# label = ttk.Label(window, text = 'raccoon', image = image_tk)
# label.pack()

button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text = '    A button', image = python_dark_tk, compound = 'left')
button.pack(pady = 10)

button_ctk = ctk.CTkButton(button_frame, text = 'A button', image = img_ctk, compound = 'left')
button_ctk.pack(pady = 10)

button_frame.grid(row = 0, column = 0, sticky = 'nsew')

# canvas -> image
canvas = tk.Canvas(window, background = 'white', bd = 0, highlightthickness = 0, relief = 'ridge')
canvas.grid(column = 1, columnspan = 3, row = 0, sticky = 'nsew')

canvas.bind('<Configure>', fill_image)

# run
window.mainloop()