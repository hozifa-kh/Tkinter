from tkinter import *
from tkinter import messagebox

# Create the Main App Window
age_app = Tk()

# Change App Text
age_app.title("Age Calculator App")

# Set Dimenstions
age_app.geometry("600x400")

# Write Age Label
age_text = Label(age_app, text="Enter Your Age", height=2, font=("Arial",10))
age_text.pack()

# Age Variable
age = StringVar()

# Set Defult Value for Age 
age.set("00")

# Create The Input for The Age
age_input = Entry(age_app, width=2, font=("Arial",30), textvariable=age)
age_input.pack() # Place The Input Into The Main Window

def calc():

    # Get Age In Years
    the_age_value = age.get()

    # Get Time Units
    months = int(the_age_value) * 12
    weeks = months * 4
    days = int(the_age_value) * 365

    line1 = f"Your Age in Months Is: {months}" 
    line2 = f"Your Age in Weeks Is: {weeks}" 
    line3 = f"Your Age in Days Is: {days}"

    all_lines = [line1,line2,line3]
    
    # Show All Lines
    messagebox.showinfo("Your Age In All Time Units", "\n".join(all_lines)) 

# Create the Calculate Button 
btn = Button(age_app, text="Calculate Age", width=20, height=2, bg="#e91e63", 
fg="white", borderwidth=0, command=calc)
btn.pack()

# Run App Infinitely
age_app.mainloop()