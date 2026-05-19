import tkinter as tk 
from tkinter import *
from tkinter import ttk

#width/height

window = tk.Tk()
window.title = ("Tk")
window.geometry("450x25")
window.attributes("-topmost",True)

entry1 = tk.Entry(window,text="",width = 20)
entry2 = tk.Entry(window,text="",width = 20)
entry3 = tk.Entry(window,text="",width = 25)

label1 = tk.Label(window, text="x")
label2 = tk.Label(window, text="=")

entry1.grid(row =1, column=1)
entry2.grid(row =1, column=3)
entry3.grid(row =1, column=5)

label1.grid(row =1, column=2)
label2.grid(row =1, column=4)

window.mainloop()  