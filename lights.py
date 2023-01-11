#!/usr/bin/python3
"""Oparations of lights"""
##import RPi.GPIO as GPIO -- for RasberryPI
from time import sleep
from classes import *
from termcolor import colored
import sys


argc = len(sys.argv) - 1
if argc != 4:
    print("Usage: ./lights [numbers of lanes in this other] \
            <north> <south> <west> <east>")
    sys.exit(1)

N = northlane(int(sys.argv[1])).count
S = southlane(int(sys.argv[2])).count
W = westlane(int(sys.argv[3])).count
E = eastlane(int(sys.argv[4])).count

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