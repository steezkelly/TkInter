from tkinter import *

#Calls Tk class, root is "main window"
root = Tk()

#Prints Hello my name is Steve!
#event is something a user can do, mouse click, key pressed, etc.
def printName(event):
    print("Hello my name is Steve!")

def printNumber(event):
    print("5")

#When passing in function, make sure not to do function() just function
button_1 = Button(root, text="Print my name")
#.bind takes two parameters, eventname and what happens when event happens
#"<Button-1>" is left-click, "<Button-3>" is right-click
#When passing in function, make sure not to do function() just function
button_1.bind("<Button-1>", printName)
button_1.bind("<Button-3>", printNumber)
button_1.pack()

#mainloop() puts the window in an infinite loop, continuously displays until exit
root.mainloop()
