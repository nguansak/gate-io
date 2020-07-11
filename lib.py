import time
import os
import requests
import json
from counter import *

baseUrl = "http://192.168.10.100:5000"
# baseUrl = "http://127.0.0.1:5000"

counter = Counter(0.5)

def fileOpen(gate):
    global f
    f = open("raw_" + gate + ".csv", "a")

def logRaw(gate, no, sensor, epoch, action):
    data = "{:.6f}".format(epoch)+","+gate+","+no+","+sensor+","+action
    print("raw:"+data)
    f.write(data+"\n")
    f.flush()
    os.fsync(f)

def sendRawData(gate, no, sensor, epoch, action):
    url = baseUrl + "/gate/" + gate + "/raw"
    data = "{:.6f}".format(epoch)+","+gate+","+no+","+sensor+","+action
    response = requests.post(url, data=data)
    return response.ok

def sendJsonData(gate, no, sensor, epoch, action):
    url = baseUrl + "/gate/" + gate + "/json"
    data = { "gate": gate, "no": no, "sensor": sensor, "epoch": epoch, "action": action }
    response = requests.post(url, json={"data":[data]})
    return response.ok

def pressed(gate, no, sensor):
    def sensorPressed(*arg):
        now = time.time()
        logRaw(gate, no, sensor, now, "pressed")
        sendJsonData(gate, no, sensor, now, "pressed")
        counter.handleRealtime(gate, no, sensor, "pressed")
    return sensorPressed

def released(gate, no, sensor):
    def sensorReleased(*arg):
        now = time.time()
        logRaw(gate, no, sensor, now, "released")
        sendJsonData(gate, no, sensor, now, "released")
        counter.handleRealtime(gate, no, sensor, "released")
    return sensorReleased

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def fileClose():
    f.close()