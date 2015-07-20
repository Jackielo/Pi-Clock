from tkinter import *
import time
import string
import httplib2
from pyowm import OWM

owm = OWM(API_key=None, version='2.5', config_module=None, language=None)

FILE = "FILE LINK"

root = Tk()
root.geometry('{}x{}'.format(320, 240))
root.config(cursor="none")
root.overrideredirect(True)

clock = Label(root, font=("Digital-7", 78), fg='white', bg='black')
clock.pack(fill=BOTH, expand=1)

todo = Label(root, font=("Digital-7", 15), fg='red', bg='black')
todo.pack(fill=BOTH, expand=1)

rain = Label(root, font=("Digital-7", 15), fg='white', bg='black')
rain.pack(fill=BOTH, expand=1)

# weather
def weather():
    obs = owm.weather_at_place('Dublin,ie')
    w = obs.get_weather()
    temps = w.get_temperature(unit='celsius')
    rain.config(text=w.get_status().title() + ', ' + str(int(temps['temp'])) + 'C')
    rain.after(1800000, weather)


#Notes
def update():
    h = httplib2.Http(".cache")
    headers, content = h.request(FILE)
    wtf2 = content.decode().replace('\\n', '\n')
    todo.config(text=wtf2)
    todo.after(300000, update)


#clock
def tick():
    time2 = time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200, tick)


def catch_click(event):
    root.destroy()


tick()
update()
weather()

clock.bind("<Button-1>", catch_click)

root.mainloop()
