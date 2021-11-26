import cv2
import matplotlib.pyplot as plt

vidcap = cv2.VideoCapture('Data/testvideo.mp4')
success,image = vidcap.read()
count = 0

while cv2.waitKey(25) & 0xFF != ord('q'):
  cv2.imshow(f"Frame {count+1}",image)
  success,image = vidcap.read()
  print(f"Read frame {count}")
  count += 1