import numpy as np
import cv2
from imutils import paths
import imutils
from matplotlib import pyplot as plt

DISTANCE = 9
UNIT = 'FT'
  
# define a video capture object
vid = cv2.VideoCapture(0)
detect = cv2.QRCodeDetector()
counter = 1
N = 3

time.sleep(5)
  
while(True):

    time.sleep(5)
      
    # capture the video frame by frame
    print("PICTURE: ", counter)
    ret, frame = vid.read()
  
    # display the resulting frame
    cv2.imshow('frame', frame)
    value, points, straight_qrcode = detect.detectAndDecode(frame)
    print(value)
    print(points)
    print(straight_qrcode)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()