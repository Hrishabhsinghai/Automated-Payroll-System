import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)


while True:
    screen_img = ImageGrab.grab(bbox=(0,0,width,height))
    array_img = np.array(screen_img)
    color_img = cv2.cvtColor(array_img,cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder by Hrishabh',color_img)
    if cv2.waitKey(1)==ord('q'):
        break
    
        