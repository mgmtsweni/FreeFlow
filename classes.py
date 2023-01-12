#!/usr/bin/python3
"""file for classes needed by the light oparator"""
from time import sleep


class lanes:
    """Class to determine the number of cars in a lane"""
    def __init__(self, count):
        self.count = count
    
    def count(self):
        return self.count
 
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
    """count down to determine the waiting time."""
    while (self.count > 0):
        print (self.count)
        self.count = self.count - 1
        sleep(1)
