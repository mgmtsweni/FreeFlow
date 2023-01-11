#!/usr/bin/python3
"""function that returns the total time to change lights"""
from time import sleep


class lanes:
    """Class to determine the number of cars in a lane"""
    def __init__(self, count):
        self.count = count
    
    def count(self):
        return self.count
        """
        self.car = 4*car
        self.bike = 3*bike
        self.van = 5*van
        self.bus = 6*bus
        self.truck = 7*truck
        self.man = 2*human
            
        def class(self):
            type = [self.car, self.bike, self.man, self.van, self.bus, self.truck]
                return type
        
        def classCount(self):
            typecount = self.car + self.bike + self.man + self.van + self.bus + self.truck
                return typecount
        """

class northlane(lanes):
    """inheritance of lanes"""
    pass

class southlane(lanes):
    """inheritance of lanes"""
    pass

class westlane(lanes):
    """inheritance of lanes"""
    pass

class eastlane(lanes):
    """inheritance of lanes"""
    pass

class laneSide:
    """class to determine which lane to choose"""
    def __init__(self, north, south, west, east):
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    def side(self):
        """Returns an array of the total number of cars in a lane"""
        lanes = [self.north, self.south, self.west, self.east]
        return lanes

def countback(self):
    while (self.count > 0):
        print (self.count)
        self.count = self.count - 1
        sleep(1)
