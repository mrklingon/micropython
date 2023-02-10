# Write your code here :-)
from microbit import *

DIRS = [1, 6, 5, 4, -1, -6, -5, -4]
sprites = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
old =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
new =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

consts = [ "Camelopardalis", "Ursa Minor", "Lyra",
           "Piscis Austrinus", "Sagittarius", "Auriga",
           "Leo Minor", "Capricornus", "Bootes"]

#constellation Camelopardalis
star1 = Image(
    "10000:"
    "00000:"
    "01010:"
    "01001:"
    "01000:"
)
#constellation Ursa Minor
star2 = Image(
    "00800:"
    "03000:"
    "00300:"
    "03008:"
    "00050:"
)
#constellation Lyra
star3 = Image(
    "00010:"
    "00080:"
    "20100:"
    "00000:"
    "30300:"
)
#constellation Piscis Austrinus
star4 = Image(
    "00000:"
    "03000:"
    "80000:"
    "01112:"
    "00000:"
)
#constellation Sagittarius
star5 = Image(
    "00300:"
    "04022:"
    "30000:"
    "00030:"
    "00000:"
)
#constellation Auriga
star6 = Image(
    "03080:"
    "00002:"
    "20000:"
    "00003:"
    "05000:"
)
#constellation Leo Minor
star7 = Image(
    "00000:"
    "03001:"
    "30020:"
    "02000:"
    "00000:"
)
#constellation Capricornus
star8 = Image(
    "00007:"
    "87010:"
    "00000:"
    "05003:"
    "00030:"
)
#constellation Bootes
star9 = Image(
    "03000:"
    "30040:"
    "00030:"
    "00500:"
    "00094:"
)

ALLCONSTS = [star1, star2, star3, star4, star5, star6,
            star7, star8, star9]

def mkSprite(sprite,spot,angle):
    sprites[sprite] = spot+angle/10
    old[sprite] = display.get_pixel(spotx(spot),spoty(spot))
    display.set_pixel(spotx(spot),spoty(spot),9)

def getspot(sprite):
    return int(sprites[sprite])

def getangle(sprite):
    s = (sprites[sprite] - int(sprites[sprite] )) *10
    return int(s+.5)

def spotx(spot):
    spot = int(spot)
    sx = spot - (5 * int(spot/5))
    return sx

def spoty(spot):
    spot = int(spot)
    sy = int(spot/5)
    return sy

def limit(spot):
    if (spot>24):
        spot=spot-24

    if (spot<0):
        spot=spot+24

    return spot

def step(sprite):
        newspot = limit(getspot(sprite) + DIRS[getangle(sprite)])
        new[sprite] = display.get_pixel(spotx(newspot),spoty(newspot))
        display.set_pixel(spotx(newspot),spoty(newspot),9)
        oldf = int (old[sprite])
        if (oldf <0):
            oldf = 0
        if (oldf >9):
            oldf = 9
        display.set_pixel(spotx(getspot(sprite)),spoty(getspot(sprite)),oldf)
        old[sprite] = new[sprite]
        sprites[sprite] = getangle(sprite)/10+newspot


def rstep(sprite):
        newspot = limit(getspot(sprite) - DIRS[getangle(sprite)])
        new[sprite] = display.get_pixel(spotx(newspot),spoty(newspot))
        display.set_pixel(spotx(newspot),spoty(newspot),9)
        oldf = int (old[sprite])
        if (oldf <0):
            oldf = 0
        if (oldf >9):
            oldf = 9
        display.set_pixel(spotx(getspot(sprite)),spoty(getspot(sprite)),oldf)
        old[sprite] = new[sprite]
        sprites[sprite] = getangle(sprite)/10+newspot

def turnR(sprite):
    ang = getangle(sprite)
    ang = ang +1
    if ang > 7:
        ang = 0
    sprites[sprite] = getspot(sprite) + ang/10


def turnL(sprite):
    ang = getangle(sprite)
    ang = ang -1
    if ang < 0:
        ang = 7
    sprites[sprite] = getspot(sprite) + ang/10

def showSprite(sprite):
    old[sprite] = display.get_pixel(spotx(getspot(sprite)),spoty(getspot(sprite)))
    display.set_pixel(spotx(getspot(sprite)),spoty(getspot(sprite)),9)
