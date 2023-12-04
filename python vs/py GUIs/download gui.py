from tkinter import *
import os
import requests

def download():
    pass

root = Tk()
root.title(os.getcwd())
root.geometry("600x450")
root.configure(bg="light gray")

Label(text="Download file", font="classic 20 bold underline", bg="light gray").pack(pady=15)

f1 = Frame(root, bg="light gray")
Label(f1, text="File url:", bg="light gray", font="classic 18 bold").grid(row=1, column=1)
url_value = StringVar()
Entry(f1, textvariable=url_value).grid(row=1, column=2)

Label(f1, text="File name:", bg="light gray", font="classic 18 bold").grid(row=2, column=1)
filename_value = StringVar()
Entry(f1, textvariable=filename_value).grid(row=2, column=2)
f1.pack()

Button(root, text="Download", font="classic 10 bold", command=download).pack()

root.mainloop()
