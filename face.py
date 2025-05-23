import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

while True:
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_COMPLEX

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #scale, minNeighbors  

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        cv2.putText(frame, 'face', (x, y), font, 2, (235, 206, 135), 4, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor = 1.3, minNeighbors = 10, minSize = (60, 10), maxSize = (200, 100))
        
        mouth = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=10, minSize = (100, 10), maxSize = (200, 100))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
            cv2.putText(frame, 'eye', (x+ex, y+ey), font, 2, (0, 0, 0), 4, cv2.LINE_AA)

        
        for (mx, my, mw, mh) in mouth:
            cv2.rectangle(roi_color, (mw, my), (mx+mw, my+mh), (255, 0, 0), 5)
            cv2.putText(frame, 'mouth', (x+mx, y+my), font, 2, (0, 0, 0), 4, cv2.LINE_AA)
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()