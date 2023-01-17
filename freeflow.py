#!/usr/bin/python3
"""Oparations of lights"""
from time import sleep
from classes import *
from termcolor import colored
from Detect import *

"""Detection using images"""
N = imageDetect('detection/images/image.jpg')
S = imageDetect('detection/images/image1.jpg')
W = imageDetect('detection/images/image2.jpg')
E = imageDetect('detection/images/image3.jpg')

"""Detection using video
N = detection('detection/videos/vid0.mp4')
S = detection('detection/videos/vid1.mp4')
W = detection('detection/videos/video1.avi')
E = detection('detection/videos/video2.mp4')
"""

chooseSide = laneSide(N, S, W, E).side()

def countback(count):
    while (count > 0):
        count = count - 1
        sleep(0.5)


def switches(index):
    print(colored("Go", 'green'))
    countback(index)
    print(colored("caution", 'yellow'))
    sleep(2)
    print(colored("Stop", 'red'))
    sleep(2)


def lights(chooseSide):
    chooseSide.sort()
    while chooseSide[3] != 0:
        if chooseSide[3] == chooseSide[0] and chooseSide[0] > 0:
            chooseSide[0] = chooseSide[0] - 1
        else:
            if chooseSide[3] == N:
                print(colored("North", 'white'))
                switches(N)
            if chooseSide[3] == S:
                print(colored("south", 'white'))
                switches(S)
            if chooseSide[3] == W:
                print(colored("west", 'white'))
                switches(W)
            if chooseSide[3] == E:
                print(colored("east", 'white'))
                switches(E)
        chooseSide[3] = chooseSide[3] - 1
        lights(chooseSide)


lights(chooseSide)
