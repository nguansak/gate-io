import sqlite3
import csv
import json
from lib import dict_factory
from counter import *
from csv_db import *
from db import *
from datetime import datetime
import time

fieldnames = ("epoch","gate","no","sensor", "action")

class GateService():
    def __init__(self, reloadTime):
        #conn = sqlite3.connect('gate.db', check_same_thread=False)
        #conn.row_factory = dict_factory
        #self.conn = conn
        # self.counter = Counter()
        self.csvDb = CsvDb()
        #self.loadDb()
        today = datetime.today().strftime('%Y-%m-%d')
        path = "data/" + today

        self.db = Db(path+"/data.db")

        self.actualPeople = self.db.selectTotal()
        self.totalPeople = self.actualPeople
        if self.totalPeople < 0:
            self.totalPeople = 0

        self.reloadTime = reloadTime
        self.currentHour = -1

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            try:
                total = self.db.selectTotal()
                if total >= 0:
                    self.totalPeople
                self.taskGenerateReportRawCountInByHour()
                time.sleep(self.reloadTime)
            except Error as e:
                print(e)

    def loadDb(self):
        self.gate = self.loadTable("gate")
        
    def loadTable(self, name):
        data = {}
        with open( "data/" + name + ".csv", 'r' ) as theFile:
            reader = csv.DictReader(theFile)
            for rows in reader:
                id = rows['id']
                data[id] = rows
        return data

    def gateInfo(self, gateCode):
        try:
            return self.gate[gateCode]
        except:
            return {}

    def handleGateRaw(self, gateCode, rawData):
        print(rawData)
        
        reader = csv.DictReader( rawData)
        for row in reader:
            print("reader", row)
        # self.csvDb.saveRaw(rawData)
        # self.counter.count(rawData)

    def handleGateJson(self, gateCode, data):
        self.csvDb.saveJson(gateCode, data["data"])
        #self.counter.count(gateCode, data["data"])

    def handleGateCounter(self, gateCode, data):
        year, month, day, hour = map(int, time.strftime("%Y %m %d %H").split())
        data['rt'] = data['t']
        data['t'] = time.time()
        data['dt'] = time.strftime('%Y-%m-%d %H:%m:%S')
        data['dir_old'] = data['dir']
        data['d'] = day
        data['h'] = hour

        if data['dir'] == 0:
            if data['gate'] == 'in':
               data['dir'] = 1

            if data['gate'] == 'out1' or data['gate'] == 'out2':
                data['dir'] = -1

        self.csvDb.saveCount(gateCode, data)
        self.db.insertCounter(data['gate'], data['no'], data['dir_old'], data['dir'], data['t'], data['rt'], data['d'], data['h'])

        self.totalPeople = self.totalPeople + data['dir']
        self.actualPeople = self.actualPeople + data['dir']
        if self.totalPeople < 0:
            self.totalPeople = 0
        print("total: ", "{:d}".format(self.totalPeople)+ " actual: ", "{:d}".format(self.actualPeople))

    def getTotal(self):
        return  {"total":self.totalPeople, "actual": self.actualPeople}
    
    def taskGenerateReportRawCountInByHour(self):
        day, currentHour = map(int, time.strftime("%d %H").split())
        
        if self.currentHour != currentHour:
            print("currentHour", currentHour)
            self.currentHour = currentHour
            self.generateReportRawCountInByHour(currentHour)

    def generateReportRawCountInByHour(self, currentHour):
        row = self.db.rawCountInByHour(currentHour)
        self.csvDb.saveReportRawCountInByHour(row)