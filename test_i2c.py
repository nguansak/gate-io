from smbus import SMBus
import time

# https://www.instructables.com/id/Raspberry-Pi-I2C-Python/
# https://www.abelectronics.co.uk/kb/article/1092/i2c-part-3---i-c-tools-in-linux
# enable i2c
# apt-get install i2c-tools python-smbus
# sudo i2cdetect -y 1

bus = SMBus(1)  # Create a new I2C bus

i2caddress1 = 0x38  # Address of MCP23017 device
i2caddress2 = 0x39  # Address of MCP23017 device

BUT_MASK = 0x01FF

while (True):
    data1 = bus.read_byte_data(i2caddress1, BUT_MASK)
    data2 = bus.read_byte_data(i2caddress2, BUT_MASK)
    print("{0:08b}".format(data1), "{0:08b}".format(data2), data1 >> 0 & 1, data1 >> 1 & 1, data1 >> 7 & 1)

   