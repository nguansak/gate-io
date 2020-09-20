from smbus import SMBus
from adafruit_debouncer import Debouncer
import time

BUT_MASK = 0x01FF

class I2cButton:
    def __init__(self, address, nums, interval=0.010):
        self.data = 0
        self.nums = nums
        self.signel = []
        self.busMask = 0
        slef.bus = SMBus(1)
        
        for i in range(this.nums):
            self.signel[i] = Debouncer(readSignal(i))
            self.busMask += i

    self readSignal(self, pos):
        def readData(*arg):
            return self.data >> pos & 1
        return readData

    def update:
        self.data = bus.read_byte_data(i2caddress1, BUT_MASK)

        for i in range(this.nums):
            this.signel[i].update()

            

    return ss.digital_read(crickit.SIGNAL1)
 


 while True:
    switch.update()
    if switch.fell:
        print('Just pressed')
    if switch.rose:
        print('Just released')
    if switch.value:
        print('not pressed')
    else:
        print('pressed')
