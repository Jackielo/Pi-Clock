# Pi-Clock
Uses the Raspberry Pi as a clock.

Adafruit PiTFT display panel required to display the clock optimally. 

Internet access also required for some functions to work.

This program is written with Python 3.2 with the Tkinter, Requests and httplib2 plugins.

Tkinter is built in with Python.

Weather API: https://developer.forecast.io/

Request: http://docs.python-requests.org/en/latest/

Httplib2: https://github.com/jcgregorio/httplib2

Font used: Digital-7


As the name says it's a Clock, but it also syncs with a txt file located on my webserver, which it then reads the content and displays it on the screen. This is done with Httplib2.

The contents of the file is structured accordingly.

Weather is also displayed on the screen by using Requests to grab the weather information from Dark Sky Forecast API and displayed.

The two functions can be switched from one and another from just a tap of the screen.

Only one function can be displayed at a time alongside the clock, due to screen resolution limits.
