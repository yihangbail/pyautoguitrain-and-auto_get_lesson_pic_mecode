import pyautogui as pi
x,y=pi.position()
print(x,y)
while True:
    x1,y1=pi.position()
    if x1!=x or y1!=y:
        print(x1,y1)
        x=x1
        y=y1