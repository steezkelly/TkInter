from tkinter import *

# Calls Tk class, root is "main window"
root = Tk()

photo = PhotoImage(file="img.png")
label = Label(root, image=photo)
label.pack()

# mainloop() puts the window in an infinite loop,
# continuously displays until exit
root.mainloop()
