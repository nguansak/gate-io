import time
import os

f = open("raw.csv", "a")

def logRaw(gate, no, sensor, epoch, action):
    data = "{:.6f}".format(epoch)+","+gate+","+no+","+sensor+","+action
    print("raw:"+data)
    f.write(data+"\n")
    f.flush()
    os.fsync(f)

def pressed(gate, no, sensor):
    def sensorPressed():
        now = time.time()
        logRaw(gate, no, sensor, now, "pressed")
    return sensorPressed

def released(gate, no, sensor):
    def sensorReleased():
        now = time.time()
        logRaw(gate, no, sensor, now, "released")
    return sensorReleased
