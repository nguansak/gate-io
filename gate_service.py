import sqlite3
import csv
import json
from lib import dict_factory
from counter import *
from csv_db import *

fieldnames = ("epoch","gate","no","sensor", "action")

class GateService():
    def __init__(self):
        conn = sqlite3.connect('gate.db', check_same_thread=False)
        conn.row_factory = dict_factory
        self.conn = conn
        # self.counter = Counter()
        self.csvDb = CsvDb()
        self.loadDb()
        self.totalPeople = 0

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
        self.csvDb.saveCount(gateCode, data)
        self.totalPeople = self.totalPeople + data['dir']
        if self.totalPeople < 0:
            self.totalPeople = 0
        print("Total = ", "{:d}".format(self.totalPeople))

    def getTotal(self):
        return self.totalPeople