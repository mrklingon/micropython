# Imports go at the top
from microbit import *
from universe import *
import music
import time
import speech
diam = 20
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
sx = 2
sy = 2
dirs = [north,east,south,west]

dir = north

while True:
    if (button_a.was_pressed() and button_b.was_pressed()) or accelerometer.was_gesture('shake'):
        if dir != stop:
            dir = stop
        else:
            if cosmos[spot(x+sx,y+sy)]>0:
                display.scroll(names[spot(x+sx,y+sy)])
                speech.say(names[spot(x+sx,y+sy)])
    else:
        if button_b.is_pressed():
            sy = sy + 1
            if sy > 4:
                sy = 0
        if button_a.is_pressed():
            sx = sx + 1
            if sx > 4:
                sx = 0
                
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
    display.set_pixel(sx,sy,9)
    time.sleep(.25)
