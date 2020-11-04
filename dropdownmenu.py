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


b = StevesButtons(root)
#mainloop() puts the window in an infinite loop, continuously displays until exit
root.mainloop()
