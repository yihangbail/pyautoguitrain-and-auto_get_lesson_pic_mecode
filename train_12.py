#更简单的中文输出
import pyautogui as pi
import time
import pyperclip

pi.click(300,300)
time.sleep(1)

a="大风程序员"
pyperclip.copy(a)
pi.hotkey('ctrl', 'v')
