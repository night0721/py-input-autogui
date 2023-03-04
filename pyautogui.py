import pyautogui
import time

time.sleep(5)
while True:
    for index in range(5):
        if pyautogui.locateOnScreen(f"q_q{index + 1}.png") is not None:
            q_center = pyautogui.center(pyautogui.locateOnScreen(f"a_q{index + 1}.png"))
            pyautogui.moveTo(q_center, duration=1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(537, 858, duration=1)
            pyautogui.click()
            time.sleep(1)
