import pyautogui as pi
pi.alert('准备好创建一个新的python文件了吗？','创建一个新的python文件','准备好了')
pi.click(76,24,duration=1)
pi.click(70,140,duration=1)
pi.click(500,447,duration=1)
a=pi.prompt("请输入文件名称：",'文件命名','test')
pi.write(a)
pi.press('enter')
pi.alert('创建成功')
