#!/usr/bin/python3
"""Oparations of lights"""
##import RPi.GPIO as GPIO -- for RasberryPI
from Detect import *

"""
def iteration(count):
    for i in range(len(count)):
        for j in range(i+1, len(count)):
            if count[i] == count[j]:
                return True
            else:
                print(count[i], count[j])

chooseSide = laneSide(8, 9, 2, 1).side() 
iteration(chooseSide)


class laneSide:
    class to determine which lane to choose
    def __init__(self, north, south, west, east):
        self.north = north
        self.south = south
        self.west = west
        self.east = east
    
    def side(self):
        #Returns an array of the total number of cars in a lane
        lanes = [self.north, self.south, self.west, self.east]
        return lanes
    
    def iteration(self):
        lanes = [self.north, self.south, self.west, self.east]
        for i in range(len(lanes)):
            for j in range(i+1, len(lanes)):
                if lanes[i] == lanes[j]:
                    print("stoping bbecause", lanes[i], "and", lanes[j], "are the same")
                else:
                    print(lanes[i], lanes[j])

class countdown(laneCount):
    def countback(self):
        while (self.count > 0):
            print (self.count)
            if laneSide(9, 5, 2, 3).iteration() is True:
                break
            self.count = self.count - 1
            sleep(1)
"""
# Python3 code to iterate over a list
"""
def recus(chooseSide):
    chooseSide.sort()
    print(chooseSide)
    while chooseSide:
        if chooseSide[3] == chooseSide[0]:
            if chooseSide[1] == chooseSide[2]:
                return chooseSide[3]
        else:
            chooseSide[3] = chooseSide[3] - 1
        recus(chooseSide)
"""
video = 'detection/videos/video1.avi'
def mytest():
    index = detection(video)
    indi =  imageDetect()
    print("this is index {} and this is image {}".format(index, indi))

mytest()