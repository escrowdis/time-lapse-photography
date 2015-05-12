import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('frame now', frame)
    c = cv2.waitKey(0);
    if c & 0xFF == ord('q'):
        break
    elif c & 0xff == ord('s'):
        file = "./" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
        cv2.imwrite(file, frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

