from gpiozero import Button
from time import sleep
from lib import *
from signal import pause

BOUNCE_TIME=0.05
MAX_TIME=0.05

gate = "in"
p1a = 6
p1b = 13
p2a = 19
p2b = 26
p3a = 20
p3b = 21
p4a = 16
p4b = 12

fileOpen(gate)

button1a = Button(p1a)
button1b = Button(p1b)
button2a = Button(p2a)
button2b = Button(p2b)
button3a = Button(p3a)
button3b = Button(p3b)
button4a = Button(p4a)
button4b = Button(p4b)

button1a.when_pressed = pressed(gate, 1, 'a')
button1b.when_pressed = pressed(gate, 1, 'b')
button2a.when_pressed = pressed(gate, 2, 'a')
button2b.when_pressed = pressed(gate, 2, 'b')
button3a.when_pressed = pressed(gate, 3, 'a')
button3b.when_pressed = pressed(gate, 3, 'b')
button4a.when_pressed = pressed(gate, 4, 'a')
button4b.when_pressed = pressed(gate, 4, 'b')

button1a.when_released = released(gate, 1, 'a')
button1b.when_released = released(gate, 1, 'b')
button2a.when_released = released(gate, 2, 'a')
button2b.when_released = released(gate, 2, 'b')
button3a.when_released = released(gate, 3, 'a')
button3b.when_released = released(gate, 3, 'b')
button4a.when_released = released(gate, 4, 'a')
button4b.when_released = released(gate, 4, 'b')
pause()
fileClose()
