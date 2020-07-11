import sqlite3
import csv
from lib import dict_factory
from counter import *

class GateService():
    def __init__(self):
        conn = sqlite3.connect('gate.db', check_same_thread=False)
        conn.row_factory = dict_factory
        self.conn = conn
        self.counter = Counter()

        self.loadDb()

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
        self.counter.count(rawData)


