"""
Use tkinter to create a GUI that allows the user to scrub through
frames in the video and choose the start time and the end time.
Then, calculate the amount of time between the start and the end.
"""
import cv2
import time
import tkinter as tk

# Load the video frames into a list
cap = cv2.VideoCapture("Data/testvideo.mp4")
framelist = []
counter = 1
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) + 1
start = time.time()
while True:
    print(f"Loading frame {counter} of {frameCount}")
    ret, frame = cap.read()
    if not ret:
        break
    framelist.append(cv2.resize(frame, (640, 480)))
    counter += 1

print(f"Finished loading videos in {time.time() - start} seconds")

# Scrub through the frames and choose the start and the end
start = None
end = None

index = 0
while not end:
    # Display the frame
    cv2.imshow("Frame", framelist[index])
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
    # Pressing right arrow key will move to next frame
    elif cv2.waitKey(0) & 0xFF == ord("d"):
        index += 1
        print("Moving to next frame")
    # Pressing left arrow key will move to previous frame
    elif cv2.waitKey(0) & 0xFF == ord("a"):
        index -= 1
        print("Moving to previous frame")
    # Pressing up arrow key will move to first frame
    elif cv2.waitKey(0) & 0xFF == ord("w"):
        index = 0
        print("Moving to first frame")
    # Pressing down arrow key will move to last frame
    elif cv2.waitKey(0) & 0xFF == ord("s"):
        index = frameCount - 22
        print("Moving to last frame")
    # Press 1 to set the start time
    elif cv2.waitKey(0) & 0xFF == ord("1"):
        start = index
        print(f"Start index set to frame #{start}")
    # Press 2 to set the end time
    elif cv2.waitKey(0) & 0xFF == ord("2"):
        end = index
        print(f"Start index set to frame #{end}")

print(f"Startframe: {start}; Endframe: {end}")

def getTimeDifference(start, end, framerate):
    return (end - start) / framerate
print("Frame rate:", cap.get(cv2.CAP_PROP_FPS))
print(f"Time difference: {getTimeDifference(start, end, cv2.CAP_PROP_FPS)} seconds")

# Create a GUI to scrub through the video using a timeline that you
