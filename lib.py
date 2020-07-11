import time
import os
import requests
import json

baseUrl = "http://192.168.10.100:5000"

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
    data = { "gate": gate, "no": no, "sensor": sensor, "epoch": epoch, "action": action }
    response = requests.post(url, json={"data":[data]})
    return response.ok

def pressed(gate, no, sensor):
    def sensorPressed(*arg):
        now = time.time()
        logRaw(gate, no, sensor, now, "pressed")
        sendRawData(gate, no, sensor, now, "pressed")
    return sensorPressed

def released(gate, no, sensor):
    def sensorReleased(*arg):
        now = time.time()
        logRaw(gate, no, sensor, now, "released")
    return sensorReleased

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def fileClose():
    f.close()