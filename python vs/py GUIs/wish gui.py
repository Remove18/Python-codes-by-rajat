from tkinter import *
import os
import time
from tkinter import messagebox as tmsg
import win32com.client as wc

speaker = wc.Dispatch("SAPI.SpVoice")

def wish():
    h = int(time.strftime("%H"))
    if (h <= 3):
        Label(root, text="this is midnight time, go to bed!", font="classic 14 bold").pack()
        speaker.speak("this is midnight time, go to bed!")
    elif (h <= 11):
        Label(root, text="this is morning time, have a good morning!", font="classic 14 bold").pack()
        speaker.speak("this is morning time, have a good morning!")
    elif (h <= 15):
        Label(root, text="this is afternoon time, have a good afternoon!", font="classic 14 bold").pack()
        speaker.speak("this is afternoon time, have a good afternoon!")
    elif (h <= 19):
        Label(root, text="this is evening time, have a good evening!", font="classic 14 bold").pack()
        speaker.speak("this is evening time, have a good evening!")
    else:
        Label(root, text="this is night time, have a good sleep!", font="classic 14 bold").pack()
        speaker.speak("this is night time, have a good sleep!")
    
root = Tk()
root.title(os.getcwd())
root.geometry("600x400")

Label(text=time.strftime("%H:%M"), font="classic 24 bold underline").pack()

wish()

root.mainloop()
