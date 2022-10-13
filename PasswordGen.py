import tkinter as tk
from tkinter import messagebox  
import random
import string
import os
import subprocess 

#adding the generated password to the clipboard for PC
def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

#adding password to clipboard for mac
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)

#Getting input from user on the numbr of characters wanted in password
def Passwords():
    while True:
            try:
                e = entry1.get()
                e = int(e)
                pas = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + '!@#$%^&*()', k = e))
                protect = str(pas)
                try:
                    copy2clip(protect)
                except:
                    addToClipBoard(protect)
                label1 = tk.Label(window, text= protect)
                canvas1.create_window(200, 100, window=label1)
                window.after(15000, label1.destroy)
                break
            except: 
                label1 = tk.Label(window, text = "Enter an Integer Value")
                canvas1.create_window(200, 208, window=label1)
                window.after(3000, label1.destroy)
                break

# creating window GUI with name
window = tk.Tk()
window.title('Password Generator')

#making entry box for user and customizing window color/size
canvas1 = tk.Canvas(window, width = 400, height =  300, bg = 'black')
canvas1.pack()
entry1 = tk.Entry(window)
canvas1.create_window(200, 150, window = entry1)

#error windwo that will pop up
error = tk.Label(window, text = "Enter an integer value")

#Creating button to generate a password
button1 = tk.Button(text='Generate Password', bg = 'blue', command = Passwords)
canvas1.create_window(200, 180, window=button1)

#Button to quit app
button2 = tk.Button(text='Quit', bg = 'red', command = window.destroy)
canvas1.create_window(200, 240, window=button2)

window.mainloop() 
