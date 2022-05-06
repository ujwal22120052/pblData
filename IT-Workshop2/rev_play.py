import cv2

# Create a VideoCapture object to read the video file
capture = cv2.VideoCapture('E:/Afreen.mp4')

# check for camera openning
if capture.isOpened() is False:
    print("Error opening video")

# Get the total number of frames
frame_idx = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
print("Starting Frame: '{}'".format(frame_idx))

# Read until video is finished:
while capture.isOpened() and frame_idx >= 0:

    # Set the current frame position to start:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

    # Capture frame-by-frame from the video:
    ret, frame = capture.read()

    if ret is True:
        # Display the frame:
        cv2.imshow('Frame in Reverse', frame)

        # Reduce the index to read next frame:
        frame_idx = frame_idx - 1
        print("Next index: '{}'".format(frame_idx))

        # Press q on keyboard to exit the program:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Break the while loop
    else:
        break

# Release the VideoCapture object:
capture.release()
cv2.destroyAllWindows()
