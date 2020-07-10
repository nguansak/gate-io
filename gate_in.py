from gpiozero import Button
from time import sleep
from lib import *
from signal import pause

BOUNCE_TIME=0.1
MAX_TIME=0.05

gate = "in"
p1a = 6
p1b = 13
p2a = 19
p2b = 26
p3a = 20
p3b = 21

button1a = Button(p1a, bounce_time=BOUNCE_TIME)
button1b = Button(p1b, bounce_time=BOUNCE_TIME)
button2a = Button(p2a, bounce_time=BOUNCE_TIME)
button2b = Button(p2b, bounce_time=BOUNCE_TIME)
button3a = Button(p3a, bounce_time=BOUNCE_TIME)
button3b = Button(p3b, bounce_time=BOUNCE_TIME)

button1a.when_pressed = pressed(gate, '1', 'a')
button1b.when_pressed = pressed(gate, '1', 'b')
button2a.when_pressed = pressed(gate, '2', 'a')
button2b.when_pressed = pressed(gate, '2', 'b')
button3a.when_pressed = pressed(gate, '3', 'a')
button3b.when_pressed = pressed(gate, '3', 'b')

pause()
f.close()
