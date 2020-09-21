import time
import json
import threading
import requests
from async_call import AsyncCall

baseUrl = "http://192.168.1.100:5000"
# baseUrl = "http://127.0.0.1:5000"


class Counter():
    def __init__(self, timeout=1):
        self.timeout = timeout
        self.map = {}
        self.sendDataAsync = AsyncCall(self.sendCountData)

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # find 
            timeout = self.timeout

            for key in self.map.keys():
                val = self.map[key]

                # print(key, val["s"])
                if val["s"] == "entered":
                    diff = val["exp"] - time.time()
                    if diff < 0:
                        self.endSession(key, timeout)
                    elif diff < timeout:
                        timeout = diff

            # print("wake again in {:.6f}".format(timeout) + "s")
            time.sleep(timeout)

    def count(self, gateCode, data):
        for row in data:
            self.handle(row['gate'], row['no'], row['sensor'], row['epoch'], row['action'])

    def handle(self, gate, no, sensor, epoch, action):
        code = gate + "{:d}".format(no) + sensor
        print({ code, gate, no, sensor, epoch, action})
        
    def handleRealtime(self, gate, no, sensor, action):
        now = time.time()

        # print({gate, no, sensor, action})

        code = gate + "{:d}".format(no)
        
        if not code in self.map.keys():
            self.map[code] = { "ta": 0,  "tb": 0, "sa": 0, "sb": 0, "s": "idle", "gate": gate, "no": no, "last": 0.0, "a": 0, "b": 0, "exp":0, "in": "", "out": "", "pat": ""  }
        # t = time, s = state

        val = self.map[code]

        diff = 0.0
        if val["last"] > 0.0:
            diff = now - val["last"]
        data = "{:.6f}".format(now)+","+gate+","+"{:d}".format(no)+","+sensor+","+action+","+"{:.6f}".format(diff)
        # print("counter:" + data)
        val['diff'] = diff

        val["last"] = now
        if val["s"] == "idle": # Start New
            if action == "pressed":
                val["s"] = "entered"
                val["t"] = now
                val[sensor] = 1
                val["exp"] = now + self.timeout
                val["in"] = sensor
        elif val["s"] == "entered":
            if action == "released":
                val["out"] = sensor
                val["exp"] = now + self.timeout
                val[sensor] = 0
        self.map[code] = val

        if action == "pressed":
            pat = sensor.upper()
            val["pat"] = val["pat"] + sensor.upper()
        if action == "released":
            pat = sensor.upper()
            val["pat"] = val["pat"] + sensor

        self.dumpState(val)
        # print("------>", val)

    def endSession(self, code, now):
        val = self.map[code]
        val["s"] = "final"
        self.map[code] = val

        dir = 0
        if val["a"] == 0 and val["b"] == 0:
            if val["in"] == "a" and val["out"] == "b":
                dir = 1
            elif val["in"] == "b" and val["out"] == "a":
                dir = -1

        data = { "gate": val["gate"], "no": val["no"], "dir": dir, "t": val["t"] }
        # print("END: " + json.dumps(data))

        # print("=====> END", val)
        self.dumpState(val)

        # self.sendCountData(val["gate"], val["no"], dir, val["t"], val["pat"])
        self.sendDataAsync.run(val["gate"], val["no"], dir, val["t"], val["pat"])

        val["s"] = "idle"
        val["pat"] = ""
        val["last"] = now
        self.map[code] = val

        # + ', ' + val["in"] + ', ' + "{:.6f}".format(val["diff"])  +
    def dumpState(self, val):
        s = val["s"]
        print('==>' + val["gate"] + "{:d}".format(val["no"]) + ', s:' + s[0:3] + ', in:' + val["in"] + ', out:' + val["out"] +", diff:{:.6f}".format(val["diff"]) + '(' + val["pat"] + ')' )

    def sendCountData(self, gate, no, dir, epoch, pat):
        url = baseUrl + "/gate/" + gate + "/counter"
        data = { "gate": gate, "no": no, "t": epoch, "dir": dir, "pat": pat }
        csv = "COUNT:"+"{:.6f}".format(epoch)+","+"{:4s}".format(gate)+","+"{:d}".format(no)+','+"{:d}".format(dir)+","+pat
        print(csv,"\n")
        try:
            response = requests.post(url, json=data)
            return response.ok
        except:
            print ("Cannot send data to server")