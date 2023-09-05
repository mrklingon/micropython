# Imports go at the top
from microbit import *
from complex import *
from space import *
import random
import time

display.scroll('Complex')

x=random.randrange(6)
y=random.randrange(6)

initall()
create(uni1)
slant(x,y)
disp(0,0)
Finished = False


def bounce():
    global x,y
    x=random.randrange(6)
    y=random.randrange(6)
    disp(x,y)


while not Finished:

    if button_a.is_pressed():
        rotateI()
        disp(x,y)
    if button_b.is_pressed():
        slant(x,y)
        disp(x,y)
    if accelerometer.was_gesture("shake"):
        Finished=True
    if accelerometer.was_gesture("left"):
        x = x-1
        if x<-10:
            x=-10
        disp(x,y)
    if accelerometer.was_gesture("right"):
        x = x+1
        if x>5:
            x=5
        disp(x,y)
    if accelerometer.was_gesture("up"):
        y=y-1
        if y<-10:
            y=-10
        disp(x,y)
    if accelerometer.was_gesture("down"):
        y = y+1
        if y>5:
            y=5
        disp(x,y)
    time.sleep(.2)
