__author__ = 'Kbobob'
from tkinter import *
import time
import datetime
import httplib2
import requests



root = Tk()
#root.geometry('{}x{}'.format(320, 240))
#root.config(cursor="none")
#root.overrideredirect(True)

clock = Label(root, font=("Digital-7", 78), fg='white', bg='black')
clock.pack(fill=BOTH, expand=1)

info = Label(root, font=("Digital-7", 15), fg='red', bg='black', justify=LEFT)
info.pack(fill=BOTH, expand=1)


default = 0
n = 0

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
        global n
        n += 1
        r = requests.get('https://api.forecast.io/forecast/80880d12ade6f9490da4d06a21c1074c/53.4519,-6.1987?units=si')
        w_dict = r.json()
        status = w_dict["currently"]["summary"] + ', ' + str(w_dict["currently"]["temperature"]) + '°C' + '\n\nMax: ' \
                 + str(w_dict["daily"]["data"][0]["temperatureMax"]) + '°C Min: ' + str(w_dict["daily"]["data"][0]["temperatureMin"]) + '°C ' \
                 + '\n\n' + datetime.datetime.fromtimestamp(w_dict["daily"]["data"][1]["sunriseTime"]).strftime('%m-%d') + "    " + str(w_dict["daily"]["data"][1]["summary"]) + '\n\n'  \
                 + datetime.datetime.fromtimestamp(w_dict["daily"]["data"][2]["sunriseTime"]).strftime('%m-%d') + "    " + str(w_dict["daily"]["data"][2]["summary"]) + '\n\n' \
                 + datetime.datetime.fromtimestamp(w_dict["daily"]["data"][3]["sunriseTime"]).strftime('%m-%d') + "    " + str(w_dict["daily"]["data"][3]["summary"])
        #get current weather
        info.config(font=("Digital-7", 15), text=status, justify=CENTER)
        info.after(200, update)

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
