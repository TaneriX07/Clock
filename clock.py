from tkinter import *
import time

root = Tk()
root.title('Clock')

def get_time():
    tm = time.strftime("%I:%M:%S %p")
    label.config(text=tm)
    label.after(1000, get_time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor=CENTER)

get_time()

root.mainloop()