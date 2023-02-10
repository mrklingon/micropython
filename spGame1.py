# Write your code here :-)
from sprites import *
import time
import random


mkSprite(5,0,1)
mkSprite(6,24,5)

display.show(ALLCONSTS[5])
showSprite(5)
showSprite(6)

def ramble(sprite):
    for i in range(1, 2+random.randrange(6)):
        step(sprite)
        time.sleep(.2)
        if random.randrange(2) > 0:
            turnL(sprite)
        else:
            turnR(sprite)


mkSprite(0,12,0)
CNT = 0

while True:
    if button_a.was_pressed():
        step(0)

    if button_b.was_pressed():
        turnR(0)

    ramble(5)
    ramble(6)

    CNT = CNT +1

    if CNT > 50:
        display.show(ALLCONSTS[random.randrange(9)])
        showSprite(0)
        showSprite(5)
        showSprite(6)
        CNT = 0

