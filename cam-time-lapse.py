
import numpy as np
import cv2
import os
import datetime

cap = cv2.VideoCapture(0)

# gap between each image
gap = 5 * 60 * 1000 # ms

count = 0

# folder path setting
folderName = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

folderPath = os.getcwd() + "/" + folderName

if not os.path.isdir(folderPath):
    os.mkdir(folderPath)

while True:

    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the resulting frame
    file = folderPath + "/" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    cv2.imwrite(file, frame)
#    cv2.imshow('frame now', frame)
    if cv2.waitKey(gap) & 0xFF == ord('q'):
        break

    count = count + 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()





