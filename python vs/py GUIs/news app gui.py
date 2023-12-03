from tkinter import *
import os
import requests
from tkinter import messagebox as tmsg

def search():
    query = newstype_value.get()
    description = description_value.get()
    content = content_value.get()
        
    url = f"https://newsapi.org/v2/everything?q={query}&popularity&apiKey=d1f69ee125ac4256bf0c651883d3dafa"
    news = requests.get(url).json()
    
    text.config(state=NORMAL)
    i = 0
    for article in news["articles"]:
        print(f"\n {i+1}. {article["title"]} :\n")
        text.insert(END, f"\n {i+1}. {article["title"]} :\n")
        print(f"{article["description"]}\n") if description == 1 else ""
        text.insert(END, f"{article["description"]}\n") if description == 1 else ""
        print(article["content"]) if content == 1 else ""
        text.insert(END, article["content"]) if content == 1 else ""
        text.insert(END, "\n")
        i = i + 1
    text.config(state=DISABLED)
    
def clear():
    text.config(state=NORMAL)
    text.delete(1.0, END)
    text.config(state=DISABLED)

root = Tk()
root.title(os.getcwd())
root.geometry("820x600")
root.configure(bg="light gray")

Label(text="-: News App By Rajat :-", font="classic 20 bold underline", fg="blue", bg="light gray").pack(pady=10)

f1 = Frame(root, width=400, height=25, bg="light gray")
Label(f1, text="News Type:", font="classic 14 bold", bg="light gray").grid(row=1, column=1, padx=3)

newstype_value = StringVar()
newstype_entry = Entry(f1, textvariable=newstype_value, width=18, font="classic 12 bold")
newstype_entry.grid(row=1, column=2, padx=10)

description_value = IntVar()
content_value = IntVar()

Label(f1, text="Description", font="classic 12 bold", bg="light gray").grid(row=1, column=3)
description_on_off = Radiobutton(f1, text="On", value=1, variable=description_value, bg="light gray").grid(row=1, column=4, padx=5)
description_on_off = Radiobutton(f1, text="Off", value=0, variable=description_value, bg="light gray").grid(row=1, column=5, padx=5)

Label(f1, text="/", font="classic 12 bold", fg="brown", bg="light gray").grid(row=1, column=6, padx=3)

Label(f1, text="Content", font="classic 12 bold", bg="light gray").grid(row=1, column=8)
content_on_off = Radiobutton(f1, text="On", value=1, variable=content_value, bg="light gray").grid(row=1, column=9, padx=5)
content_on_off = Radiobutton(f1, text="Off", value=0, variable=content_value, bg="light gray").grid(row=1, column=10, padx=5)

Button(f1, text="Search", font="classic 12 bold", fg="blue", command=search).grid(row=1, column=11, padx=3)
f1.pack(pady=8, padx=15)

Label(root, text="-:Results:-", font="classic 14 bold underline", fg="purple", bg="light gray").pack(pady=2)

Button(root, text="Clear", font="classic 8 bold", command=clear).pack(pady=8)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill="both", pady=12)

text = Text(root, width=100, height=50, yscrollcommand=scrollbar.set, wrap="word")
text.configure(font="classic 14 bold")
text.pack(fill=BOTH, padx=25, pady=12)
text.config(state=DISABLED)

scrollbar.config(command=text.yview)

root.mainloop()
