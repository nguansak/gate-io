from i2c_button import I2cButton
from signal import pause

i2caddress1 = 0x38

def pressed(pos):
    def func():
        print(pos, 'pressed ##')
    return func

def released(pos):
    def func():
        print(pos, 'released ##')
    return func

buttons1 = I2cButton(i2caddress1, 8)
buttons1.whenPressed(0, pressed(0))
buttons1.whenReleased(0, released(0))

pause()