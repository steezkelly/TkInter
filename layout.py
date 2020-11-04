from tkinter import *

#Calls Tk class
root = Tk()

#Frame, invisible rectangle(container) to put "things" in
#.pack packs it all into the frame
topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

#Widgets
#fg(foreground) optional, sets text color
button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green" )
button4 = Button(botFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

#mainloop() puts the window in an infinite loop, continuously displays until exit
root.mainloop()
