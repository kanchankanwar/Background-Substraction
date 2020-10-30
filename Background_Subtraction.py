import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
cap = cv2.VideoCapture('C:/v2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
looper,image=cap.read()
count=0
looper=True
size = 600, 400
for count in range (0,100):
    looper,image=cap.read()
    print('Read a new frame: ', looper)
    count+1
    if(count==10):
        cv2.imwrite("frame%d.jpg" % count, image)
        img = Image.open("frame%d.jpg"%count)
        img2=img.rotate(90)
        img2.thumbnail(size, Image.ANTIALIAS)
        img2.save("img02.jpg")
        break
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    imS = cv2.resize(frame, (400, 300)) 
    imS2 = cv2.resize(fgmask, (400, 300)) 
    cv2.imshow('ORIGINAL VIDEO',imS)
    cv2.imshow('SUBTRACTED OUTPUT',imS2)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break    
img=cv2.imread("frame10.jpg")
cap.release()
cv2.destroyAllWindows()
def sendImg():
    img=cv2.imread("img02.jpg")
    return img
