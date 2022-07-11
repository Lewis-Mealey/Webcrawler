import mouse
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(0.1)

mouse.move(138,220, absolute=True, duration=0.1)
mouse.double_click()

mouse.move(535,245, absolute=True, duration=0.5)
mouse.double_click()

time.sleep(0.3)

for char in "SCM - W":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.05)

mouse.move(250,300, absolute=True, duration=0.1)
mouse.double_click()

time.sleep(0.5)

mouse.move(780,640, absolute=True, duration=0.2)
mouse.click()

time.sleep(0.2)

mouse.move(772,694, absolute=True, duration=0.2)
mouse.click()

time.sleep(0.5)

mouse.move(770,603, absolute=True, duration=0.1)
mouse.click()

time.sleep(0.1)

for char in "Nitec Security Suite":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.01)

mouse.move(720,660, absolute=True, duration=0.1)
mouse.click()

mouse.move(780,620, absolute=True, duration=0.5)
mouse.click()

mouse.move(207,216, absolute=True, duration=0.3)
mouse.click()

mouse.move(1600,185, absolute=True, duration=0.1)