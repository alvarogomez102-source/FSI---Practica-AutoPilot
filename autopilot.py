
import cv2
import numpy as np

# Capture video
cap = cv2.VideoCapture("imgs/PracticaAutoPilot.mp4")

while(1):

    # Read each frame
    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (400, 300))

    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find edges using Canny detector
    edges = cv2.Canny(gray, 50, 200)

    # Detect lines using Hough transform
    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi/180,
        100,
        minLineLength=150,
        maxLineGap=10
    )

    # Draw detected lines on the original frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line

            cv2.line(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 0, 0),
                3
            )

    # Display original video with detected lines
    cv2.imshow('Lane Detection', frame)

    # Display Canny edges
    cv2.imshow('Edges', edges)

    # Stop with ESC
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

# Close windows
cap.release()
cv2.destroyAllWindows()
