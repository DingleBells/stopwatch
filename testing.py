import cv2


# Function to scroll through frames in a video by pressing arrow keys

def scrollVideo(filepath):
    cap = cv2.VideoCapture(filepath)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()