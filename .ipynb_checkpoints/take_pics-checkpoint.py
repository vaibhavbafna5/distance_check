"""
This script will take 'N' pictures w/ webcam & save them.
Change the 'MODE' string to indicate the kind of lighting situation.

Example mode options:
    - no_light
    - low_light_5ft
    - mid_light
    - high_light_9ft
    - etc

Images are saved under the 'webcam_imgs' directory.
The picture is taken when the 'q' key is pressed.
"""

import cv2
import time

DISTANCE = 9
UNIT = 'FT'
  
# define a video capture object
vid = cv2.VideoCapture(0)
counter = 1
N = 3

time.sleep(5)
  
while(counter <= N):

    time.sleep(5)
      
    # capture the video frame by frame
    print("PICTURE: ", counter)
    ret, frame = vid.read()
  
    # display the resulting frame
    cv2.imshow('frame', frame)
    img_name = f'webcam_img_{DISTANCE}_{UNIT}_{counter}.png' 
    cv2.imwrite(img_name, frame)
    counter += 1

vid.release()
cv2.destroyAllWindows()