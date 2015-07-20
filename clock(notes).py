from tkinter import *
import time
import string
import httplib2

FILE = "http://www.kingbob.org/todo.txt"

root = Tk()
root.geometry('{}x{}'.format(320, 240))
root.config(cursor="none")
root.overrideredirect(True)

clock = Label(root, font=("Digital-7",78), fg='white', bg='black')
clock.pack(fill=BOTH, expand=1)

todo = Label(root, font=("Digital-7", 15), fg='red', bg='black', justify=LEFT)
todo.pack(fill=BOTH, expand=1)

def update():
	h = httplib2.Http(".cache")
	headers, content = h.request(FILE)
	wtf2 = content.decode().replace('\\n', '\n')
	todo.config(text=wtf2)
	todo.after(300000, update)

def tick():
	time2 = time.strftime('%H:%M:%S')
	clock.config(text=time2)
	clock.after(200, tick)

def catch_click(event):
	root.destroy()
tick()
update()

clock.bind("<Button-1>", catch_click)


root.mainloop()
