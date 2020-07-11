class Counter():
    # def __init__(self):
    #     self.map

    def count(self, gateCode, data):
        for row in data:
            self.handle(row['gate'], row['no'], row['sensor'], row['epoch'], row['action'])

    def handle(self, gate, no, sensor, epoch, action):
        code = gate + "{:d}".format(no) + sensor
        print({ code, gate, no, sensor, epoch, action})
        