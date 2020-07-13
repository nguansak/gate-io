import sqlite3
from sqlite3 import Error

sql_create_counter_table = """
    CREATE TABLE IF NOT EXISTS counter (
        id integer PRIMARY KEY AUTOINCREMENT,
        gate TEXT NOT NULL,
        no INTEGER NOT NULL,
        t REAL NOT NULL,
        rt REAL NOT NULL,
        dir INTEGER NOT NULL
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

        
    def initDb(self):
        self.execMutate(sql_create_counter_table)
  
    def insertCounter(self, gate, no, dir, t, rt):
        sql = "INSERT INTO counter (gate, no, dir, t, rt) VALUES ('" + gate + "'," + "{:d}".format(no) +  "," + "{:d}".format(dir) + "," + "{:.6f}".format(t) + "," + "{:.6f}".format(rt) + ");"
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