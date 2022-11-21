import cv2
import numpy as np

cap = cv2.VideoCapture('filmik.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mpv4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)
out = cv2.VideoWriter('filmik_RB.mp4', fourcc, 50.0, size, True)


while(1):

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([107,50,50])
    upper_blue = np.array([130,255,255])


    lower_red1=np.array([0, 190, 50])
    upper_red1=np.array([5, 255, 255])
    
    lower_red2=np.array([170, 170, 50])
    upper_red2=np.array([179, 255, 255])
     

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask3 = cv2.inRange(hsv, lower_red2, upper_red2)
    res = cv2.bitwise_and(frame,frame, mask= mask|mask2|mask3)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    out.write(res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

cap.release()
out.release()
print("Video saved successfully.")
cv2.destroyAllWindows() 


