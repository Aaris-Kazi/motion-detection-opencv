import cv2
import numpy as np

cap = cv2.VideoCapture('test1.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dil = cv2.dilate(threshold, None,iterations=3)
    contours, _ = cv2.findContours(dil, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (l,b,d,h)= cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 5900:
            continue
        cv2.rectangle(frame1, (l, b), (l+d, b+h), (0,255,0), 2)
        cv2.putText(frame1, 'Status {}'.format('moment'), (10, 20), cv2.FONT_HERSHEY_COMPLEX,
        1,(0,0,255),3)
    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    cv2.imshow('inter', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()