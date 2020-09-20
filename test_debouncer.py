from adafruit_debouncer import Debouncer
from smbus import SMBus
import time

# https://www.instructables.com/id/Raspberry-Pi-I2C-Python/
# enable i2c
# apt-get install i2c-tools python-smbus.

bus = SMBus(1)  # Create a new I2C bus

i2caddress1 = 0x38  # Address of MCP23017 device
i2caddress2 = 0x39  # Address of MCP23017 device

BUT_MASK = 0x01FF

def readSignal:
    data = bus.read_byte_data(i2caddress1, BUT_MASK)
    return data1 >> 1 & 1

signal = Debouncer(readSignal)

while True:
    signal.update()

    if signal.fell:
        print('Just pressed')
    if signal.rose:
        print('Just released')
    if !signal.value:
        print('pressed')
    else:
        print('pressed')
