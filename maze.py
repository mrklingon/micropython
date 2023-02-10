from microbit import *
import speech
import random

x=2
y=2

display.set_pixel(x,y,8)

while True:
    oldx = x
    oldy = y
    if accelerometer.is_gesture("up"):
        x = x-1
        if x<0:
            x=0

    if accelerometer.is_gesture("down"):
        x = x+1
        if x>4:
            x=4

    if accelerometer.is_gesture("left"):
        y = y-1
        if y<0:
            y=0

    if accelerometer.is_gesture("right"):
        y = y+1
        if y>4:
            y=4


    display.set_pixel(oldx,oldy,0)
    display.set_pixel(x,y,8)



