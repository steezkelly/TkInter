import tkinter as tk

window = tk.Tk()

window.title("My APP")

window.geometry("400x400")

#LABEL
title = tk.Label(text="Hello world. Welcome to my APP")
title.grid(column=0, row=0)

# BUTTON
button1 = tk.Button(text="Click Me")
button1.grid(column=0, row=1)

#Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

window.mainloop()
