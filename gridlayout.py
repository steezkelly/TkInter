from tkinter import *

#Calls Tk class, root is "main window"
root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

#Entry creates blank field user can input in
entry_1 = Entry(root)
entry_2 = Entry(root)

#.grid puts it in a grid, takes row and optional column argument
#sticky aligns element in a container to certain direction (N,E,W,S)
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

#.grid puts it in a grid, takes row and optional column argument
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

#Checkbox, columnspan takes up multiple column cells
c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

#mainloop() puts the window in an infinite loop, continuously displays until exit
root.mainloop()
