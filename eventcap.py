from tkinter import *
import random

root = Tk()

def key(event):
  print ("pressed", repr(event.char))

def callback(event):
  frame.focus_set()
  print ("clicked at", event.x, event.y)

def a_pressed(event):
    print("You are love")

def r_pressed(event):
    rnum = random.randint(0, 9)
    rm = ["I love you", "You are great", "Wow you are stunning",
    "God Bless you", "Let's make love", "Let's make lots of money",
    "Keep motivated you are great", "Keep learning", "Keep steady",
    "You will be Blessed soon"]
    print(rm[rnum])



frame = Frame(root, width=300, height=300)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.bind("a", a_pressed)
frame.bind("r", r_pressed)
frame.pack()

root.mainloop()
