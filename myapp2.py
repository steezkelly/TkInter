#This file adds the pieces to the window
import tkinter as tk

window = tk.Tk()

#Adds a title to the window
window.title("My Awesome App!")

#Sizes the window when first appears, measured in pixels
window.geometry("300x300")

#----LABELS-----
prompt = tk.Label(text="Welcome to my app\nHello User", font=("Times New Roman", 20))
prompt.grid()

#----Entry Fields----
entry_field = tk.Entry()
entry_field.grid()

#----BUTTONS----
button1 = tk.Button(text="Click me", bg="green")
button1.grid()

#----TEXT FIELDS----
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()

#Makes the frame appear on screen. Akin to calling a function
window.mainloop()
