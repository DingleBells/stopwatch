# Play a video and display the frame number on the top right corner
import cv2
import numpy as np

cap = cv2.VideoCapture('Data/testvideo.mp4')

frameNum = 1
# Lock the frame size to 640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
while True:
    ret, frame = cap.read()
    # Display the frame number on the top right corner
    cv2.putText(frame, str(frameNum), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    if ret == False:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frameNum += 1
