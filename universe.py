# Your new file!
from microbit import *
import random

cosmos = []

def initUni(diam):
    global cosmos
    global dia

    dia = diam
    
    for x in range (diam * diam):
        if random.randrange(100)>60:
            cosmos.append(random.randrange(5))
        else:
            cosmos.append(0)

def showxy(x,y):
    global cosmos
    global dia
    
    display.clear()
    for dy in range(5):
        for dx in range(5):
            cell = x+dx+(y+dy)*dia
            if cosmos[cell]>0:
                display.set_pixel(dx,dy,5+cosmos[cell])

