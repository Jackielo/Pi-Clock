__author__ = 'Kbobob'
from tkinter import *
import time
import string
import httplib2
from pyowm import OWM

owm = OWM(API_key=None, version='2.5', config_module=None, language=None)

root = Tk()
root.geometry('{}x{}'.format(320, 240))
root.config(cursor="none")
root.overrideredirect(True)

clock = Label(root, font=("Digital-7", 78), fg='white', bg='black')
clock.pack(fill=BOTH, expand=1)

info = Label(root, font=("Digital-7", 15), fg='red', bg='black', justify=LEFT)
info.pack(fill=BOTH, expand=1)


default = 0

#Notes
def update():
    global default
    if default == 0:
        FILE = "FILE LINK"
        h = httplib2.Http(".cache")
        headers, content = h.request(FILE)
        wtf2 = content.decode().replace('\\n', '\n')
        info.config(text=wtf2)
        info.after(300000, update)
    else:
        obs = owm.weather_at_place('Dublin,ie')
        w = obs.get_weather()
        temps = w.get_temperature(unit='celsius')
        info.config(text=w.get_status().title() + ', ' + str(int(temps['temp'])) + 'C')
        info.after(1800000, update)

#clock
def tick():
    time2 = time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200, tick)


def catch_click(event):
    root.destroy()

def switch(event):
    global default
    if default == 0:
        default = 1
        update()
    else:
        default = 0
        update()


tick()
update()
#weather()

info.bind("<Button-1>", switch)
clock.bind("<Button-1>", catch_click)


root.mainloop()
