from microbit import *
from universe import *
import time
import speech
diam = 20 #universe is 20x20
initUni(diam) #initialize universe

for x in range(5):
    showxy(x,x)
    time.sleep(.33)

display.scroll("Star Traveler",delay=60)
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
    #stop/start motion with A+B or "shake"
    if (button_a.was_pressed() and button_b.was_pressed()) or accelerometer.was_gesture('shake'):
        if dir != stop:
            #save current direction
            sav = dir
            dir = stop
        else:
            #restore motion
            if dir == stop:
                dir = sav
            
    else:
        if button_b.is_pressed() and dir == stop:
            #say the name if stopped at a star
           if cosmos[spot(x+sx,y+sy)]>0:
                speech.say(names[spot(x+sx,y+sy)])
               
        if button_a.is_pressed()and dir == stop:
            #print the name if stopped at a star
           if cosmos[spot(x+sx,y+sy)]>0:
                display.scroll(names[spot(x+sx,y+sy)])

    #navigate "ship" on screen if motion stopped
    #if in motion - set direction to the tilt direction
    if accelerometer.was_gesture('up'):
        if dir!= stop:
            dir=north
        else:
            sy = sy - 1
            if sy < 0:
                sy = 0
    if accelerometer.was_gesture('down'):
        if dir!= stop:
            dir=south
        else:
            sy = sy + 1
            if sy > 4:
                sy = 4
        
    if accelerometer.was_gesture('right'):
        if dir!= stop:
            dir=west
        else:
            sx = sx + 1
            if sx > 4:
                sx = 4
                
    if accelerometer.was_gesture('left'):
        if dir!= stop:
            dir=east
        else:
            sx = sx - 1
            if sx < 0:
                sx = 0
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

#display stars at the current x,y
    showxy(x,y)
    display.set_pixel(sx,sy,9)
#display ship at current sx,sy location
    time.sleep(.25)
