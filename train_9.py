#键盘
import pyautogui as pi
import time
pi.click(300,300)
time.sleep(1)

# #不支持直接输入中文输入，模拟键盘中字母的位置输入
# pi.write('100000hefefef')
# #中文输入
# pi.write('100wshr \n')

pi.write('100wshr',0.2)