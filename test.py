from gpiozero import Button
from time import sleep
import time
import os
from signal import pause
f = open("raw.csv", "a")


BOUNCE_TIME=0.05
MAX_TIME=0.05

p1a = 21
p1b = 13

button1a = Button(p1a)
button1b = Button(p1b)

time1a = 0
time1b = 0

def logRaw(sensor, epoch):
    print("raw:"+"{:.6f}".format(epoch)+","+sensor)
    f.write("{:.6f}".format(epoch)+","+sensor+"\n")
    f.flush()
    os.fsync(f)

def pressed(sensor):
    def sensorPressed():
        now = time.time()
        logRaw(sensor, now)
    return sensorPressed

def released(sensor):
    def sensorReleased():
        now = time.time()
        logRaw(sensor, now)
    return sensorReleased

def say1a():
    global time1a, time1b
    logRaw("1a")
    if (time1b>0):
        delta = time.time() - time1b
        print("delta: ", delta)
        if (delta>MAX_TIME):
            print("Gate 1 IN")
        time1b = 0
        time1a = 0
    else:
        time1a = time.time()
        
def say1b():
    global time1a, time1b
    logRaw("1b")
    if (time1a>0):
        delta = time.time() - time1a
        print("delta: ", delta)
        if (delta>MAX_TIME):
            print("Gate 1 OUT")
        time1b = 0
        time1a = 0
    else:
        time1b = time.time()


button1a.when_pressed = pressed('1a')
button1b.when_pressed = pressed('1b')

# button1.when_released = say1r
# button2.when_released = say2r
# while True: 
#     if button1.is_pressed: 
#         print("Button 1 is pressed") 
#         sleep(0.25)
#     if button2.is_pressed: 
#         print("Button 2 is pressed") 
#         sleep(0.25)

pause()
f.close()