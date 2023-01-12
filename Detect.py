#!/usr/bin/python3
from numpy import *
import cv2


cascade_src = 'detection/weights/cars.xml'


def detection(filename):
    """function for video detection"""
    rectangle = []
    cascade = cv2.CascadeClassifier(cascade_src)

    vc = cv2.VideoCapture(filename)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        frameHeight, frameWidth, fdepth = frame.shape

        frame = cv2.resize(frame, (600, 400))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cars = cascade.detectMultiScale(gray, 1.3, 3)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        count = 0
        for value in cars:
            count += 1

        cv2.imshow("Results", frame)

        if cv2.waitKey(33) == ord('q'):
            break

    vc.release()
    return count


def imageDetect(filename):
    
    vehicle_cascade = cv2.CascadeClassifier(cascade_src)
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in vehicles:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    count = 0
    for value in vehicles:
        count += 1

    cv2.imshow('img', img)
    cv2.waitKey()
    return count
