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

label1.place(x = 80, y = 10)
label2.place(x = 45, y = 110)
label3.place(x = 160, y = 40)

window.mainloop()