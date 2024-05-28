import numpy as np
import cv2 as cv

# Define a function to calculate the Euclidean distance
def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize video capture
videoCapture = cv.VideoCapture("/Users/janavbhasin/desktop/rugved/rugved_ai/balltracking/ball_tracking_example.mp4")
prevCircle = None

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break

    # Manipulate the color channels
    frame_ = frame.copy()
    frame_[:, :, 0] = 0  # Set blue channel to 0
    frame_[:, :, 2] = 0  # Set red channel to 0
    frame_[:, :, 1] = frame[:, :, 1] * (frame[:, :, 1] > 110)  # Threshold green channel

    # Convert to grayscale
    grayframe = cv.cvtColor(frame_, cv.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurframe = cv.GaussianBlur(grayframe, (55, 55), 0)

    # Apply dilation
    kernel = np.ones((5, 5), np.uint8)
    blurframe = cv.dilate(blurframe, kernel, iterations=1)

    # Detect circles using HoughCircles
    circles = cv.HoughCircles(blurframe, cv.HOUGH_GRADIENT, 1.2, 100, param1=50, param2=30, minRadius=10, maxRadius=150)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            if prevCircle is not None:
                # Choose the circle closest to the previous circle
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) > dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i

        # Draw the chosen circle
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)  # Small circle at center
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (225, 0, 225), 3)  # Circle outline
        prevCircle = chosen

    # Display the frame
    cv.imshow("circles", frame)

    # Exit loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
videoCapture.release()
cv.destroyAllWindows()
