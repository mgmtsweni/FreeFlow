#!/usr/bin/python3
"""function that returns the total time to change lights"""
from time import sleep


class lanes:
    """Class to determine the number of cars in a lane"""
    def __init__(self, count):
        self.count = count
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
        #Returns an array of the total number of cars in a lane
        lanes = [self.north, self.south, self.west, self.east]
        return lanes
    
    """def iteration(self):
        lanes = [self.north, self.south, self.west, self.east]
        for i in range(len(lanes)):
            for j in range(i+1, len(lanes)):
                if lanes[i] == lanes[j]:
                    print("stoping bbecause", lanes[i], "and", lanes[j], "are the same")
                else:
                    return"""

class countdown:
    def __init__(self, count, lane2):
        self.count = count
        self.lane2 = lane2

    def countback(self):
        while (self.count > 0):
            # print (self.count)
            if self.count != self.lane2:
                self.count = self.count - 1
                sleep(1)
            else:
                print ("changing lanes")
                break
        return (self.count)


class lanecmp:
    """class to determine which lane to choose"""
    def __init__(self, north, south, west, east):
        self.north = north
        self.south = south
        self.west = west
        self.east = east
