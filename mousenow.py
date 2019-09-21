import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print("鼠标移动到左上角退出")
def mouse_position():
    try:
        while(True):
            #TODO:
            x,y = pyautogui.position()
            im = pyautogui.screenshot()
            positonobj = "X:" + str(x).rjust(4) + " Y:" + str(y).rjust(4) + '\t' + "color: " + str(im.getpixel((x,y)))
            print(positonobj,end="")
            print('\b'*len(positonobj),end='',flush = True)
            if x ==0 and y == 0:
                break
    except KeyboardInterrupt:
        print("\nDone")

if __name__ == "__main__":
    while(True):
        n = input("enter> ")
        if n == 'p':
            mouse_position()
        elif n == 'a':
            pass
        elif n == 'q':
            exit(1)
        else:
            print('try again!')
        

