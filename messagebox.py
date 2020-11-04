from tkinter import *
import tkinter.messagebox

# Calls Tk class, root is "main window"
root = Tk()
#Messagebox, takes Window Title and displays text
tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 300 years")
#Stores yes/no in answer variable
answer = tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")
#Prints silly face if answer is "yes"
if answer == "yes":
    print(" @..@ ")

# mainloop() puts the window in an infinite loop,
# continuously displays until exit
root.mainloop()
