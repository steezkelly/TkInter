from tkinter import *

# Calls Tk class, root is "main window"
root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

greenBox = canvas.create_rectangle(25, 25, 125, 60, fill="green")
blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")

canvas.delete(redLine)
canvas.delete(ALL)


# mainloop() puts the window in an infinite loop,
# continuously displays until exit
root.mainloop()
