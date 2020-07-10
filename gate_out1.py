from gpiozero import Button
from time import sleep
import time
import os
from signal import pause
from lib import *

BOUNCE_TIME=0.1

gate = 'out1'
p1a = 20
p1b = 21

button1a = Button(p1a, bounce_time=BOUNCE_TIME)
button1b = Button(p1b, bounce_time=BOUNCE_TIME)

time1a = 0
time1b = 0

button1a.when_pressed = pressed(gate, '1', 'a')
button1b.when_pressed = pressed(gate, '1', 'b')

pause()
f.close()