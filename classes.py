from tkinter import *


class StevesButtons:
#__init__(self) special function, initialize automatically an object
#master means root/mainwindow pass it in for GUI, creates root/mainwindow
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

#use self to create widgets/buttons
        self.printButton = Button(frame, text="Print Message",
        command=self.printMessage)
        self.printButton.pack(side=LEFT)

#.quit is built into Tkinter, .quit closes window
        self.quitButton = Button(frame, text="Quit",
         command=frame.quit)
        self.quitButton.pack(side=LEFT)

#self Whenever we create object from class StevesButtons,
#throw this object in there
    def printMessage(self):
        print("Wow, this actually worked!")

#Calls Tk class, root is "main window"
root = Tk()

#Anytime we want to use something from a class, we need to make an object
#Object allows us to access stuff in class, set object to classname
#pass in the root window/main window gets treated as master
#__init__ gets called automatically as soon as we create any object from class
b = StevesButtons(root)
#mainloop() puts the window in an infinite loop, continuously displays until exit
root.mainloop()
