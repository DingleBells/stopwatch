import cv2
import time

# Function to scroll through frames in a video by pressing arrow keys

def scrollVideo(filepath):
    cap = cv2.VideoCapture(filepath)
    framelist = []
    counter = 1
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))+1
    start = time.time()
    while True:
        print(f"Loading frame {counter} of {frameCount}")
        ret, frame = cap.read()
        if not ret:
            break
        framelist.append(cv2.resize(frame, (640, 480)))
        counter += 1

    print(f"Finished loading videos in {time.time() - start} seconds")
    counter = 0
    while True:
        # Lock frame size to 640x480
        cv2.imshow("Frame", framelist[counter])
        # Display frame number in top right corner
        cv2.putText(framelist[counter], f"Frame {counter + 1} of {frameCount}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        if cv2.waitKey(0) & 0xFF == ord("q"):
            break
        # Press ing right arrow key will move to next frame
        elif cv2.waitKey(0) & 0xFF == ord("d"):
            counter += 1
            print("Moving to next frame")
        # Pressing left arrow key will move to previous frame
        elif cv2.waitKey(0) & 0xFF == ord("a"):
            counter -= 1
            print("Moving to previous frame")
        # Pressing up arrow key will move to first frame
        elif cv2.waitKey(0) & 0xFF == ord("w"):
            counter = 0
            print("Moving to first frame")
        # Pressing down arrow key will move to last frame
        elif cv2.waitKey(0) & 0xFF == ord("s"):
            counter = frameCount-1
            print("Moving to last frame")

    cap.release()
    cv2.destroyAllWindows()


scrollVideo("Data/testvideo.mp4")