__author__ = 'Kbobob'
from tkinter import *
import time
import string
import httplib2
from pyowm import OWM

owm = OWM(API_key=None, version='2.5', config_module=None, language=None)

root = Tk()
#root.geometry('{}x{}'.format(320, 240))
#root.config(cursor="none")
#root.overrideredirect(True)

clock = Label(root, font=("Digital-7", 78), fg='white', bg='black')
clock.pack(fill=BOTH, expand=1)

info = Label(root, font=("Digital-7", 15), fg='red', bg='black', justify=LEFT)
info.pack(fill=BOTH, expand=1)


default = 0

#Notes
def update():
    global default
    if default == 0:
        FILE = "http://www.kingbob.org/todo.txt"
        h = httplib2.Http(".cache")
        headers, content = h.request(FILE)
        wtf2 = content.decode().replace('\\n', '\n')
        info.config(font=("Digital-7", 15), text=wtf2, justify=LEFT)
        info.after(300000, update)
    else:
        #get current weather
        obs = owm.weather_at_place('Dublin,ie')
        w = obs.get_weather()
        temps = w.get_temperature(unit='celsius')
        #get forecast
        fc = owm.daily_forecast('Dublin, ie', limit=4)
        f = fc.get_forecast()
        lst = f.get_weathers()

        day1date = str(lst[1])
        day1status = str(lst[1])
        day1date = day1date[54:59]
        day1status = day1status[80:-1]
        day2date = str(lst[2])
        day2status = str(lst[2])
        day2date = day2date[54:59]
        day2status = day2status[80:-1]
        day3date = str(lst[3])
        day3status = str(lst[3])
        day3date = day3date[54:59]
        day3status = day3status[80:-1]
        print('\n' + day1date + ' ' + day1status + ' ' + day2date + ' ' + day2status + ' ' + day3date + ' ' + day3status)

        #for weather in f:
        #    print(weather.get_reference_time('iso')[5:10], weather.get_detailed_status())
        status = w.get_detailed_status().title() + ', ' + str(int(temps['temp'])) + '°C' + '\n\nMax: ' \
                 + str(int(temps['temp_max'])) + '°C Min: ' + str(int(temps['temp_min'])) + '°C' + '\n\n' \
                 + day1date + ' : ' + day2date + ' : ' + day3date + '\n' \
                 + day1status + ' : ' + day2status + ' : ' + day3status
        info.config(font=("Digital-7", 30), text=status, justify=CENTER)
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

info.bind("<Button-1>", switch)
clock.bind("<Button-1>", catch_click)


root.mainloop()
