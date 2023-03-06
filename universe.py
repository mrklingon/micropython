# Your new file!
from microbit import *
import random

cosmos = []
names = []

def initUni(diam):
    global cosmos
    global dia
    global names

    dia = diam
    
    for x in range (diam * diam):
        if random.randrange(100)>60:
            cosmos.append(random.randrange(5))
            names.append(placeNM())
        else:
            cosmos.append(0)
            names.append("")

def showxy(x,y):
    global cosmos
    global dia
    
    display.clear()
    for dy in range(5):
        for dx in range(5):
            cell = x+dx+((y+dy)*dia)
            if cosmos[cell]>0:
                display.set_pixel(dx,dy,5+cosmos[cell])
def spot(x,y):
    cell = x+(y*dia)
    return (cell)

    
def placeNM():
    
    start = ["Gi","Ro","Ah","Mi","Pa","Ki","Re","Sy","Th","Zo"]
    mid = ["eu","af","gh","uu","a","e","i","o","u","y"]
    end = ["nk","as","of","z","d","n","ll","ah","ei","ie"]

    Place = random.choice(start)+random.choice(mid)+random.choice(end)
    return (Place)
