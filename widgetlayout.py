from tkinter import *

#Calls Tk class, root is "main window"
root = Tk()

#bg is background color, fg is text color/foreground
one = Label(root, text="One", bg="red", fg="white")
one.pack()

two = Label(root, text="Two", bg="green", fg="black")
#fill=X fills it as big as the X(width) value as the parent(Frame) is
two.pack(fill=X)

three = Label(root, text="Three", bg="blue", fg="white")
#fill=Y fills it as big as the Y(height) value as the parent(Frame) is
three.pack(side=LEFT, fill=Y)

#mainloop() puts the window in an infinite loop, continuously displays until exit
root.mainloop()
