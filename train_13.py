#按键的按住与抬起
import pyautogui as pi
import time

pi.keyDown('shift')
pi.write('sss')
pi.sleep(1)
pi.keyUp('shift')
pi.write('sss')