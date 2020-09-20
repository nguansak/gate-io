import sqlite3
from sqlite3 import Error

sql_create_counter_table = """
    CREATE TABLE IF NOT EXISTS counter (
        id integer PRIMARY KEY AUTOINCREMENT,
        gate TEXT NOT NULL,
        no INTEGER NOT NULL,
        t REAL NOT NULL,
        rt REAL NOT NULL,
        dir INTEGER NOT NULL,
        raw_dir INTEGER NOT NULL,
        day INTEGER,
        hour INTEGER
    ); """

class Db():
    def __init__(self, db_file):
        self.db_file = db_file
        # self.conn = None
        # try:
        #     self.conn = sqlite3.connect(db_file, check_same_thread=False)
        # except Error as e:
        #     print(e)
        # finally:
        #     if self.conn:
        #         self.conn.close()

    def execMutate(self, query):
        
        conn = None
        try:
            conn = sqlite3.connect(self.db_file, check_same_thread=False)
            c = conn.cursor()
            c.execute(query)
            conn.commit()
            c.close()
            
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def execQueryOne(self, query):
        
        conn = None
        try:
            conn = sqlite3.connect(self.db_file, check_same_thread=False)
            c = conn.cursor()
            c.execute(query)
            records = c.fetchall()

            if len(records) == 1:
                return records[0]
            return None
            
            c.close()
            
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


    def execQueryMany(self, query):
        
        conn = None
        try:
            conn = sqlite3.connect(self.db_file, check_same_thread=False)
            c = conn.cursor()
            c.execute(query)
            records = c.fetchall()

            if len(records) == 0:
                return None
            return records
            
            c.close()
            
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
        
    def initDb(self):
        self.execMutate(sql_create_counter_table)
  
    def insertCounter(self, gate, no, raw_dir, dir, t, rt, day, hour):
        sql = "INSERT INTO counter (gate, no, raw_dir, dir, t, rt, day, hour) VALUES ('" + gate + "'," + "{:d}".format(no) +  "," + "{:d}".format(raw_dir) +  "," + "{:d}".format(dir) + "," + "{:.6f}".format(t) + "," + "{:.6f}".format(rt) + "," + "{:d}".format(day)+ "," + "{:d}".format(hour)+ ");"
        self.execMutate(sql)

    def selectTotal(self):
        sql = "select sum(dir) as total from counter"
        try:
            row = self.execQueryOne(sql)
            
            if row == None:
                return 0

            total = row[0]

            if total == None:
                total = 0

            print('selectTotal', total)
            return total
        except Error as e:
            print(e)
            return 0

    def rawCountInByHour(self, hour):
        sql = "select hour, count(*) as total from counter where gate = 'in' and raw_dir = 1 and hour >= 10 and hour < 22 and hour < " + "{:d}".format(hour) + " group by hour"
        try:
            row = self.execQueryMany(sql)
            return row
        except Error as e:
            print(e)
            return None