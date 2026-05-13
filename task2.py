import tkinter as tk 
from tkinter import *
from tkinter import ttk

#width/height

window = tk.Tk()
window.title = ("T-Town Veterinary Clinic Database")
window.geometry("600x200")
window.attributes("-topmost",True)

dogphoto = PhotoImage(file="dog.png")

label1 = tk.Label(window, image=dogphoto)

label1.pack(side=LEFT)
window.mainloop()