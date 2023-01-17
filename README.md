# Freeflow 

**FreeFlow** is a Traffic light system that uses AI technology to control traffic lights and lowers traffic congestion.

# **Introduction**
With an increasing population and automobiles in cities, urban traffic congestion is becoming one of the most pressing issues. In addition to prolonging travel times and adding stress to drivers, traffic congestion also use more fuel and increase carbon dioxide air pollution. The traffic lights is one of critical elements affecting the traffic flow. Instead of being traffic-dependent, the typical traffic patterns depend on time. In this project, a traffic control system based on image processing and python code is proposed, which alters the timing of green, yellow, and red lights depending on the volume of traffic. 

# The Main Function
countback(count) is a function that takes in a single argument, count, and repeatedly decrements the value of count by 1 while count is greater than 0. It also calls the sleep(0.5) function each time through the loop. This function is used to delay the execution of subsequent code. This funtion is used to depict cars moving pass the traffic lights. 

switches(index) is a function that takes in a single argument, index. It first prints the string "Go" in green color, then calls the countback(index) function with the index argument passed in. It then prints the string "caution" in yellow color and calls the sleep(2) function twice, first to delay 2 sec then to delay 2 sec again. It then prints the string "Stop" in red color.

lights(chooseSide) is a function that takes in a single argument, chooseSide, which is a list of four integers. The function first sorts the chooseSide list in ascending order using the sort() method. It then enters a while loop that continues as long as the last element of the chooseSide list (chooseSide[3]) is not equal to 0.

It checks if the last element of the chooseSide list (chooseSide[3]) is equal to the first element of the chooseSide list (chooseSide[0]) and the first element of the chooseSide list is greater than 0, it decrements the first element of the chooseSide list by 1.

It then checks if the last element of the chooseSide list is equal to the predefined global variables N, S, W, E, and if so, it prints the corresponding string and calls the switches() function with the value of N, S, W, E passed in respectively.

Finally, it decrements the last element of the chooseSide list by 1 and recursively calls itself with the updated chooseSide list.

It is worth noting that global variables N, S, W, E are not defined in the code snippet provided.

# Blog
My project [block](https://www.linkedin.com/in/gift/mtsweni-591123a3) post

# Usage
For the interface and screen management. 
default user and password, admin and admin

```
py interface/login
```
<p align="center"><img src="interface/images/RMimage.PNG"\></p>

image.png
For the main project. run the FreeFlow function. you can edit the resources to either a picture or a video by calling the the functions in detect.py and include the relevent resources.

```
py freeflow.py
```
<p align="center"><img src="interface/images/RMimage.PNG"\></p>

# Author:
M G Mtsweni [Linkedin](https://www.linkedin.com/in/gift/mtsweni-591123a3)

# Licensing
Copyright (c) 2023 [mgtsweni](\LICENSE)
