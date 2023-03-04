from pynput.keyboard import Key, Controller
import time
keyboard = Controller()


def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


while True:
    pass
    # time.sleep(3)
    # keyboard.type('‎')
    # enter()
    # time.sleep(60)
