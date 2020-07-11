import unittest
from counter import *
from lib import *
import keyboard  # using module keyboard

counter = Counter(0.5)

# while True: 
#     try:
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break

#         if keyboard.is_pressed('a'):
#             counter.handleRealtime("in", 1, "a", "pressed")
   
#         if keyboard.is_pressed('s'):
#             counter.handleRealtime("in", 1, "b", "pressed")


#     except:
#         break  # if user pressed a key other than the given key the loop will break

from pynput.keyboard import Key, KeyCode, Listener

def on_press(key):
    if key == KeyCode.from_char("a"):
        counter.handleRealtime("in", 1, "a", "pressed")
    if key == KeyCode.from_char("s"):
        counter.handleRealtime("in", 1, "b", "pressed")

def on_release(key):
    if key == KeyCode.from_char("a"):
        counter.handleRealtime("in", 1, "a", "released")
    if key == KeyCode.from_char("s"):
        counter.handleRealtime("in", 1, "b", "released")
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()