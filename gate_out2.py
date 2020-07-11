from gpiozero import Button
from time import sleep
import time
import os
from signal import pause
from lib import *

BOUNCE_TIME=0.1

gate = 'out2'
p1a = 20
p1b = 21

fileOpen(gate)

button1a = Button(p1a)
button1b = Button(p1b)

time1a = 0
time1b = 0

button1a.when_pressed = pressed(gate, 1, 'a')
button1b.when_pressed = pressed(gate, 1, 'b')

# pressed(gate, '1', 'a')()
# pressed(gate, '1', 'b')()
# pressed(gate, '1', 'b')()
# pressed(gate, '1', 'a')()

pause()
fileClose()
