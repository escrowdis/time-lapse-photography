
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.cv.CV_FOURCC(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # write video
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame now', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


