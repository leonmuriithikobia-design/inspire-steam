from tkinter import *

def hello():
    print("Hello from Leon")

root = Tk()
root.geometry("400x400")

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one,text="Press Me!",command = hello)
button_one.pack()

root.mainloop()