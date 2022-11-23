import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics

while True:
    screen_img = ImageGrab.grab(bbox=(0,0,500,500))
    array_img = np.array(screen_img)
    color.img = cv2.cvtCOlor(array_img,cv2.color_bgr2rgb)
    cv2.imshow('Screen Recorder by Hrishabh',color_img)
    if cv2.waitKey(1)==ord('q'):
        break
    
        