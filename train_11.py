#组合按键
import pyautogui as pi
import time
pi.click(300,300)
time.sleep(1)

pi.hotkey('ctrl','a')
time.sleep(1)
pi.hotkey('ctrl','c')
time.sleep(1)
pi.press('pgdn')
time.sleep(1)
pi.write('\n\n')
pi.hotkey('ctrl','v')