import csv
import os
import json
from datetime import datetime
import time
import threading

class CsvDb():
    def __init__(self):
        self.today = time.strftime('%Y-%m-%d')
        path = "data/" + self.today
        self.f = open(path+"/raw_all.csv", "a")
        self.f_in = open(path+"/raw_in.csv", "a")
        self.f_out1 = open(path+"/raw_out1.csv", "a")
        self.f_out2 = open(path+"/raw_out2.csv", "a")
        self.f_test = open(path+"/raw_test.csv", "a")
        self.f_count = open(path+"/raw_count.csv", "a")

        # self.reportPath = "../report"
        self.reportPath = "D:\Dropbox\+JoM-Dell\Big Counting\Hour report"

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            self.f.flush()
            os.fsync(self.f)      
            self.f_in.flush()
            os.fsync(self.f_in)
            self.f_out1.flush()
            os.fsync(self.f_out1)
            self.f_out2.flush()
            os.fsync(self.f_out2)
            self.f_test.flush()
            os.fsync(self.f_test)
            time.sleep(5000)

    def saveRaw(self, gate, rawData):
        for r in rawData["data"]:
            print(r)
            csv = "{:.6f}".format(r['epoch'])+","+r['gate']+","+r['no']+","+r['sensor']+","+r['action']
            print("raw:" + csv)

    def saveJson(self, gate, jsonData):
        for r in jsonData:
            csv = "{:.6f}".format(r['epoch'])+","+r['gate']+","+"{:d}".format(r['no'])+","+r['sensor']+","+r['action']+","+"{:.6f}".format(r['diff'])
            print("raw:" + csv)
            self.saveData(gate, csv)
  
    def saveData(self, gate, rawData):
        self.f.write(rawData+"\n")
        # self.f.flush()
        # os.fsync(self.f)

        if gate == "in":
            self.f_in.write(rawData+"\n")
            # self.f_in.flush()
            # os.fsync(self.f_in)

        if gate == "out1":
            self.f_out1.write(rawData+"\n")
            # self.f_out1.flush()
            # os.fsync(self.f_out1)

        if gate == "out2":
            self.f_out2.write(rawData+"\n")
            # self.f_out2.flush()
            # os.fsync(self.f_out2)

        if gate == "test":
            self.f_test.write(rawData+"\n")
            # self.f_test.flush()
            # os.fsync(self.f_test)

    def saveCount(self, gate, r):
        # print(json.dumps(r))
        csv = "{:.6f}".format(r['t'])+","+"{:.6f}".format(r['rt'])+","+r['gate']+","+"{:d}".format(r['no'])+',"'+r['dt']+'",'+"{:d}".format(r['dir_old'])+','+"{:d}".format(r['dir'])+','+r['pat']+","+"{:.6f}".format(r['diff'])+","+"{:.6f}".format(r['duration'])
        print("count: " + csv)
        self.f_count.write(csv+"\n")
        self.f_count.flush()
        os.fsync(self.f_count)

    def saveReportRawCountInByHour(self, data):
        f_report= open(self.reportPath+"/report_by_hour_" + self.today + ".csv", "w")
        f_report.write("time,in\n")

        if data != None:
            for r in data:
                csv = '"' + "{:d}.00".format(r[0])+" - "+"{:d}.59".format(r[0])+'",'+"{:d}".format(r[1])
                print("ReportRawCountInByHour: " + csv)
                f_report.write(csv+"\n")
        f_report.flush()
        os.fsync(f_report)