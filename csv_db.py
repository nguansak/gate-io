import csv
import os
import json

class CsvDb():
    def __init__(self):
        self.f = open("raw_all.csv", "a")
        self.f_in = open("raw_in.csv", "a")
        self.f_out1 = open("raw_out1.csv", "a")
        self.f_out2 = open("raw_out2.csv", "a")
        self.f_test = open("raw_test.csv", "a")
        self.f_count = open("raw_count.csv", "a")

    def saveRaw(self, gate, rawData):
        for r in rawData["data"]:
            print(r)
            csv = "{:.6f}".format(r['epoch'])+","+r['gate']+","+r['no']+","+r['sensor']+","+r['action']
            print("raw:" + csv)

    def saveJson(self, gate, jsonData):
        for r in jsonData:
            csv = "{:.6f}".format(r['epoch'])+","+r['gate']+","+"{:d}".format(r['no'])+","+r['sensor']+","+r['action']
            print("raw:" + csv)
            self.saveData(gate, csv)
  
    def saveData(self, gate, rawData):
        self.f.write(rawData+"\n")
        self.f.flush()
        os.fsync(self.f)

        if gate == "in":
            self.f_in.write(rawData+"\n")
            self.f_in.flush()
            os.fsync(self.f_in)

        if gate == "out1":
            self.f_out1.write(rawData+"\n")
            self.f_out1.flush()
            os.fsync(self.f_out1)

        if gate == "out2":
            self.f_out2.write(rawData+"\n")
            self.f_out2.flush()
            os.fsync(self.f_out2)

        if gate == "test":
            self.f_test.write(rawData+"\n")
            self.f_test.flush()
            os.fsync(self.f_test)

    def saveCount(self, gate, r):
        print(json.dumps(r))
        csv = "{:.6f}".format(r['t'])+","+r['gate']+","+"{:d}".format(r['no'])+","+"{:d}".format(r['dir'])
        self.f_count.write(csv+"\n")
        self.f_count.flush()
        os.fsync(self.f_count)