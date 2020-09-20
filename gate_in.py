from lib import *
from signal import pause
from i2c_button import I2cButton

i2caddressA = 0x38
i2caddressB = 0x39

gate = "in"
nums = 8

fileOpen(gate)

buttonsA = I2cButton(i2caddressA, 8)
buttonsB = I2cButton(i2caddressB, 8)

for i in range(nums):
    print(i)
    buttonsA.whenPressed(i, pressed(gate, i+1, 'a'))
    buttonsA.whenReleased(i, released(gate, i+1, 'a'))
    buttonsB.whenPressed(i, pressed(gate, i+1, 'b'))
    buttonsB.whenReleased(i, released(gate, i+1, 'b'))

pause()
fileClose()
