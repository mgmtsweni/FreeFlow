#!/usr/bin/python3
"""Oparations of lights"""
##import RPi.GPIO as GPIO -- for RasberryPI
from time import sleep
from vehiclecontrol import *
from termcolor import colored
from sys import argv

"""
N = northlane(int(argv[1])).count
S = southlane(int(argv[2])).count
W = westlane(int(argv[3])).count
E = eastlane(int(argv[4])).count


The side with the bigger value would be chosen
#note0# we need to compare each side to check if they're equal
    if true then we close that side which was bigger and open the compered lane
#note1# we need to decrease the lanes by half of the total in one lane
#note2# if we have two lanes with the same number, we'll open them in the NSWE order
NSWE - North, South, West, East
"""

N = northlane(5).count
S = southlane(2).count
W = westlane(3).count
E = eastlane(4).count

chooseSide = laneSide(N, S, W, E).side()
north = chooseSide[0]
south = chooseSide[1]
west = chooseSide[2]
east = chooseSide[3]
#print("last unsorted value", east)
chooseSide.sort()
lane2 = chooseSide[1]
lane4 = chooseSide[3]
#print("last sorted value", lane4)


def switches(index):
    while True:
        print(colored("Stop", 'red'))
        sleep(2)
        green(index)
        print(colored("caution", 'yellow'))
        sleep(2)
        break 

def green(index):
    print(colored("Go", 'green'))
    lane4 = countdown(index, lane2).countback()
    return (lane4)
    #sleep(int(countlane))

while True:
    if lane4 == north:
        print("North lane")
        switches(north)
    
    elif lane4 == south:
        print("South lane:")
        switches(south)

    elif lane4 == west:
        print("West lane")
        switches(west)
 
    else:
        print("East lane")
        switches(east)
