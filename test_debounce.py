import RPi.GPIO as GPIO
from signal import pause
from lib import *
from gpio import *

p1a = 6
p1b = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(p1a, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cb(pin):
    print('pressed')

gate = "in"
# GPIO.add_event_detect(p1a, edge=GPIO.RISING, callback=pressed(gate, '1', 'a'), bouncetime=200)

def real_cb(pin):
    print('pressed')

# GPIO.setup(p1a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cb = ButtonHandler(p1a, real_cb, edge='rising', bouncetime=200)
cb.start()
GPIO.add_event_detect(p1a, GPIO.RISING, callback=pressed(gate, '1', 'a'))


pause()