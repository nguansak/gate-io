from smbus import SMBus
from adafruit_debouncer import Debouncer
import time
import threading

class I2cButton:
    def __init__(self, address, nums, interval=0.010):
        self.data = 0
        self.address = address
        self.nums = nums
        self.signel = {}
        self.pressed = {}
        self.released = {}
        self.busMask = 0
        self.bus = SMBus(1)
        
        for i in range(self.nums):
            self.signel[i] = Debouncer(self.readSignal(i))
            self.busMask = self.busMask | (1 << i)

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def readSignal(self, pos):
        def readData(*arg):
            return self.data >> pos & 1
        return readData

    def update(self):
        self.data = self.bus.read_byte_data(self.address, self.busMask)
        # print("{0:08b}".format(self.data), "{0:08b}".format(self.busMask))

    def whenPressed(self, pos, action):
        self.pressed[pos] = action

    def whenReleased(self, pos, action):
        self.released[pos] = action

    def emitPressed(self, pos):
        # print(pos, "pressed")
        if (pos in self.pressed):
            self.pressed[pos]()

    def emitReleased(self, pos):
        # print(pos, "released")
        if (pos in self.released):
            self.released[pos]()
    
    def run(self):
        while True:
            self.update()
            for i in range(self.nums):
                self.signel[i].update()
                if self.signel[i].fell:
                    self.emitPressed(i)
                if self.signel[i].rose:
                    self.emitReleased(i)
            time.sleep(0.1)