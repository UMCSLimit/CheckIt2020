import cv2
import numpy as np

video =  cv2.VideoCapture('http://212.182.27.87:8000/camera/mjpeg')
while True:
    check, frame = video.read()
    img = cv2.flip(frame, -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    x1 = 200
    y1 = 200

    x2 = 600
    y2 = 600

    # cv2.rectangle(threshold, (x1, y1), (x2, y2), (255,0,0), 2)

    # x1,y1 ------
    # |          |
    # |          |
    # |          |
    # --------x2,y2

    cv2.imshow('frame', threshold)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        video.release()
        break