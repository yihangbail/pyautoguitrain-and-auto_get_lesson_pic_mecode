import pyautogui as pi
import time
# #方案1：
# pi.moveTo(147,511,2)
# time.sleep(0.1)
# pi.mouseDown()
# pi.move(200,200)
# pi.mouseUp()
#方案2：
for i in range(3):
    pi.mouseDown(147,511,'left',1)
    time.sleep(0.1)
    pi.move(200,240,0.5)
    pi.mouseUp()

    pi.mouseDown()
    pi.move(-200, -200, 0.5)
    pi.mouseUp()

