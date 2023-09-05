import time
uni1 = []
uni2 = []
radius = 21
import random
from complex import *
from microbit import *
def initall():
    for i in range(radius*radius):
        uni1.append(0)
        uni2.append(0)

def create(universe):
    for i in range(radius*radius):
        if random.randrange(100)>75:
            universe[i]=random.randrange(9)+1

def copy(u1,u2):
    for i in range(radius*radius):
        u1[i] =u2[i]

def clearu(u1):
    for i in range(radius*radius):
        u1[i]=0


def spot(x,y):
    x2 = x+10
    y2 = y+10 
    spot = x2 + (y2*radius)
    return spot

def disp(x,y):
    global uni1
    for row in range(5):
        for col in range(5):
            s=spot(x+col,y-row)
            display.set_pixel(col,row,uni1[s])
            
            
def slant(x,y):
    for r in range(5):
        disp(x+r,y+r)
        time.sleep(.2)
    disp(x,y)
        
def rotateI():
    global uni1, uni2

    for y in range(-10,10):
        for x in range(-10,10):
            val = uni1[spot(x,y)]
            rt = mltI([x,y])
            uni2[spot(rt[0],rt[1])]=val
    copy(uni1,uni2)
