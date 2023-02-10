# Write your code here :-)
from sprites import *
import time
import random
import speech


mkSprite(5,0,1)
mkSprite(6,24,5)

KONST = 5
display.show(ALLCONSTS[KONST])
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
Score = 0
while True:
    if button_a.was_pressed():
        step(0)

    if button_b.was_pressed():
        turnR(0)

    if (getspot(0) == getspot(5)):
        Score = Score + 50
        KONST = random.randrange(9)
        display.show(ALLCONSTS[KONST])
        speech.say("score")
        speech.say(str(Score))
        showSprite(0)
        showSprite(5)
        showSprite(6)


    if (getspot(0) == getspot(6)):
        Score = Score + 50
        step(0)
        KONST = random.randrange(9)
        display.show(ALLCONSTS[KONST])
        speech.say("score")
        speech.say(str(Score))
        speech.say(consts[KONST])
        display.scroll(consts[KONST])
        display.show(ALLCONSTS[KONST])
        showSprite(0)
        showSprite(5)
        showSprite(6)
    time.sleep(.4)
    CNT = CNT +1
    if (random.randrange(9)>6):
        ramble(5)

    if (random.randrange(19)>13):
        ramble(6)

    if CNT > 50:
        display.show(ALLCONSTS[random.randrange(9)])
        showSprite(0)
        showSprite(5)
        showSprite(6)
        CNT = 0
    if accelerometer.was_gesture("shake"):
        speech.say(consts[KONST])
        display.scroll(consts[KONST])
        display.scroll("Score:")
        display.scroll(str(Score))
        display.show(ALLCONSTS[KONST])
        showSprite(5)
        showSprite(6)
        showSprite(0)
