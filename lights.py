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

N = northlane(8).count
S = southlane(4).count
W = westlane(2).count
E = eastlane(6).count

chooseSide = laneSide(N, S, W, E).side()

def countback(count):
    while (count > 0):
        print (count)
        count = count - 1
        sleep(0.5)

def switches(index):
    print(colored("Go", 'green'))
    countback(index)
    print(colored("caution", 'yellow'))
    sleep(2)
    print(colored("Stop", 'red'))
    sleep(2)

def north(N):
    print(colored("North", 'white'), N)
    switches(N)

def south(S):
    print(colored("south", 'white'), S)
    switches(S)
    
def west(W):
    print(colored("west", 'white'), W)
    switches(W)
    
def east(E):
    print(colored("east", 'white'), E)
    switches(E)

def lights(chooseSide):
    chooseSide.sort()
    print(chooseSide)
    while chooseSide[3] != 0:
        if chooseSide[3] == chooseSide[0] and chooseSide[0] > 0:
             chooseSide[0] = chooseSide[0] - 1
        else:
            if chooseSide[3] == N:
                north(N)
            if chooseSide[3] == S:
                south(S)
            if chooseSide[3] == W:
                west(W)
            if chooseSide[3] == E:
                east(E)
        chooseSide[3] = chooseSide[3] - 1
        lights(chooseSide)

lights(chooseSide)