from tkinter import *
from time import strftime

root = Tk()
root.title("clock")
root.geometry("200x200")
root.resizable(0,0)

def Clock():
    clock = strftime("%H:%M:%S %p")
    label.config(text=clock)
    label.after(1000,Clock)

label = Label(root,font="helvetica",background = "black",foreground="cyan")
label.place(x=50,y=80)

Clock()
root.mainloop()