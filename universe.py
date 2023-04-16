from microbit import *
import random

cosmos = []
names = []

def initUni(diam):
    #initialize the cosmos and names arrays
    global cosmos
    global dia
    global names

    dia = diam
    
    for x in range (diam * diam):
        if random.randrange(100)>60:
            #60% of the time create a star system
            cosmos.append(random.randrange(5))
            names.append(placeNM())
        else: #nothing here put a zero and "" in the arrays
            cosmos.append(0)
            names.append("")

def showxy(x,y):
    global cosmos
    global dia
    #display the 5x5 portion of the cosmos at x,y
    display.clear()
    for dy in range(5):
        for dx in range(5):
            cell = x+dx+((y+dy)*dia)
            if cosmos[cell]>0:
                display.set_pixel(dx,dy,5+cosmos[cell])
def spot(x,y):
    #map an x,y coordinate into the linear cosmos and name array
    cell = x+(y*dia)
    return (cell)

    
def placeNM():
    #build a random star name 
    start = ["Gi","Ro","Ah","Mi","Pa","Ki","Re","Sy","Th","Zo"]
    mid = ["eu","af","gh","uu","a","e","i","o","u","y"]
    end = ["nk","as","of","z","d","n","ll","ah","ei","ie"]

    Place = random.choice(start)+random.choice(mid)+random.choice(end)
    return (Place)
