from tkinter import *
import os

root = Tk()
root.title(os.getcwd())
root.geometry("820x600")

scrollbar = Scrollbar(root, width=20)
scrollbar.pack(side=RIGHT, fill=BOTH)

text = Text(root, yscrollcommand=scrollbar, bg="light gray")
text.pack()
scrollbar.config(command=text.yview)

text.insert(END, "Hello")
text.config(state=DISABLED)

root.mainloop()
