import tkinter as tk 
from tkinter import *
from tkinter import ttk

#width/height

window = tk.Tk()
window.title = ("Example")
window.geometry("325x150")
window.attributes("-topmost",True)

dogphoto = PhotoImage(file="dog.png")

label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window,text="A cuddly little puppy! This is from the same\n creators that brought you Keopi and Kero Kero", bg="#8fe3f7")
label3 = tk.Label(text = "Pochacco!")

label1.grid(row = 0, column = 0, columnspan = 2)
label2.grid(row = 2, column = 0)
label3.grid(row = 0, column = 1, columnspan = 2)

window.mainloop()