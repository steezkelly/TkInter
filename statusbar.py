from tkinter import *

#Calls Tk class, root is "main window"
root = Tk()


class StevesButtons:

    def doNothing():
        print("Ok ok I won't...")
#5*4*3*2*1 returns that result
    def factor5():
        n=5
        fact=1
        for i in range(1, n+1):
            fact = fact * i
        print (fact)

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

# *******  Main Menu *******

#Create menu, already built in with Tkinter
    menu = Menu(root)
#.config configures menu for "menu"
    root.config(menu=menu)
#We want dropdown functionality, aka cascade
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Project...", command=doNothing)
    subMenu.add_command(label="New", command=doNothing)
    #5*4*3*2*1
    subMenu.add_command(label="Factor5", command=factor5)
#Creates separation line in subMenu
    subMenu.add_separator()
#Quits the frame/exits the program
    subMenu.add_command(label="Exit", command=root.quit)
#Creates editMenu as a new menu
    editMenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)

# ******* Toolbar *******

    toolbar = Frame(root, bg="blue")

    insertButton = Button(toolbar, text="Insert Image", command=doNothing)
    insertButton.pack(side=LEFT, padx=2, pady=2)
    printButton = Button(toolbar, text="Print", command=doNothing)
    printButton.pack(side=LEFT, padx=2, pady=2)

    toolbar.pack(side=TOP, fill=X)

# ****** Status Bar ******
#bd stands for border, creates border around the text
#relief takes a value, SUNKEN creates sunken effect
#anchor takes a value, W is west/left (make sure text appears on left)
    status = Label(root, text="Preparing to do nothing...", bd=1,
    relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)


b = StevesButtons(root)
#mainloop() puts the window in an infinite loop, continuously displays until exit
root.mainloop()
