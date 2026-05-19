import tkinter as tk 
from tkinter import *
from tkinter import ttk

#width/height

window = tk.Tk()
window.title = ("T-Town Veterinary Clinic Database")
window.geometry("600x250")
window.attributes("-topmost",True)

dogphoto = PhotoImage(file="dog.png")

label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text = "Name", width = 16)
label3 = tk.Label(window, text = "Type", width = 16)
label4 = tk.Label(window, text = "Breed", width = 16)
label5 = tk.Label(window, text = "Owner", width = 16)
label6 = tk.Label(window, text = "Birthdate", width = 16)
label7 = tk.Label(window, text = "Client Database", width = 16)

entry1 = tk.Entry(window, text="",width = 15)
entry2 = tk.Entry(window, text="",width = 15)
entry3 = tk.Entry(window, text="",width = 15)
entry4 = tk.Entry(window, text="",width = 15)
entry5 = tk.Entry(window, text="",width = 15)
entry6 = tk.Entry(window, text="",width = 15)

button1 = tk.Button(window, text = "< Previous")
button2 = tk.Button(window, text = "Save Entry", width = 16, height = 3)
button3 = tk.Button(window, text = "Next >")
button4 = tk.Button(window, text = "Search By Name", width = 15)

#grod(row = x. column = x)
label1.grid(row = 1, column = 1)
label2.grid(row = 2, column = 1)
label3.grid(row = 2, column = 2)
label4.grid(row = 2, column = 3)
label5.grid(row = 2, column = 4)
label6.grid(row = 2, column = 5)
label7.grid(row = 1, column = 3)

entry1.grid(row = 3, column = 1)
entry2.grid(row = 3, column = 2)
entry3.grid(row = 3, column = 3)
entry4.grid(row = 3, column = 4)
entry5.grid(row = 3, column = 5)
entry6.grid(row = 0, column = 5)

button1.grid(row = 4, column = 1)
button2.grid(row = 4, column = 3)
button3.grid(row = 4, column = 5)
button4.grid(row = 0, column = 4)

window.mainloop()