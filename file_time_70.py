import xlwt
import os 
import sys 
import pyautogui
from moviepy.editor import VideoFileClip

# a = file_dir.split('\')
# file_dir = os.path.join()    


class FileClip():
    def __init__(self,file_dir):
        self.file_dir = file_dir
        os.chdir(file_dir)

    def timeConver(self,time_size):
        M,H = 60,60**2
        if time_size < M :
            return 'time : %s 秒'%str(time_size)
        elif M < time_size < H :
            return 'time : %s  分 %s 秒'%(int(time_size/M),int(time_size%M))
        else:
            a = int(time_size/H)
            b = int(time_size%H/M)
            c = int(time_size%H%M)
            return 'time: %s时 %s分 %s秒'%(a,b,c)

    def get_file_time(self,filename):
        clip = VideoFileClip(filename)
        time = self.timeConver(clip.duration)
        return time

class GuiOperate():
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
    def getPosition(self):
        
        try:
            while(True):
                x,y = pyautogui.position()
                im = pyautogui.screenshot()
                col = im.getpixel((x,y))
                positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4) + ' color:' + str(col)
                print(positionStr,end='')
                print('\b'*len(positionStr),end = '',flush = True)
        except KeyboardInterrupt:
            print('DONE \n')


if __name__ == "__main__":
    # file_dir = str(input('输入视频目录： '))
    # print(os.getcwd())
    # file = FileClip(file_dir)
    # print(os.getcwd())
    mouse = GuiOperate()
    mouse.getPosition()