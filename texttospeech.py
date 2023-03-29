from tkinter import *
from gtts import gTTS
import os

root = Tk()
root.geometry("350x250") 
root.configure(bg='white')
root.title("Sountext - TEXT TO SPEECH")

Label(root, text = "Text to Speech", font = "arial 20 bold underline ", bg='white').pack()
Label(text ="Manjeet Kumar", font = 'arial 8 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text to convert", font = 'arial 10 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

def Text_to_speech():
    Message = entry_field.get()
    language='en'
    speech = gTTS(text = Message,lang=language,slow=False)
    speech.save('sound.mp3')
    os.system('sound.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4', bg='green').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'red').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset,bg='yellow').place(x=175 , y = 140)

root.mainloop()
