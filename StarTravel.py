# Imports go at the top
from microbit import *
from universe import *
import time
diam = 30
initUni(diam)

for x in range(5):
    showxy(x,x)
    time.sleep(.33)

north = 0
east = 1
south = 2
west = 3
stop = 5

x=0
y=0

dirs = [north,east,south,west]

dir = north

while True:
    if button_a.was_pressed() and button_b.was_pressed():
        dir = stop
    if accelerometer.was_gesture('up'):
        dir=north
    if accelerometer.was_gesture('down'):
        dir=south
    if accelerometer.was_gesture('right'):
        dir=west
    if accelerometer.was_gesture('left'):
        dir=east
    
    if dir == west:
        x=x-1
        if x<0:
            x=diam-5
    
    if dir == east:
        x=x+1
        if x>diam+1:
            x=0
   
    if dir == north:
        y=y-1
        if y<0:
            y=diam-5
    if dir == south:
        y=y+1
        if y>diam-5:
            y = 0     


    showxy(x,y)
    time.sleep(.25)
