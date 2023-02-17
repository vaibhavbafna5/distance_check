import numpy as np
import cv2
from imutils import paths
import imutils
from matplotlib import pyplot as plt
import time

DISTANCE = 9
UNIT = 'FT'
  
# define a video capture object
vid = cv2.VideoCapture(0)

def find_markers_v2(image):
    print("entering find_markers_v2")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    
    contours = cv2.findContours(
        edged.copy(),
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:50]
    final_contours = []
    
    # print("contours: ", contours)
    
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * peri, True)
        
        if len(approx) == 4:
            final_contours.append(contour)
    
    # print(final_contours)
    # cv2.drawContours(image, final_contours, -1, (0, 255, 0), 2)
    # plt.imshow(image)
    # plt.show()

    return final_contours
    
    # cv2.waitKey(0)
    
#     plt.imshow(image)
#     plt.show()
    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print("contours: ", contours)
  
while(True):
      
    # capture the video frame by frame
    ret, frame = vid.read()
  
    # display the resulting frame
    final_contours = find_markers_v2(frame)
    cv2.drawContours(frame, final_contours, -1, (0, 255, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()