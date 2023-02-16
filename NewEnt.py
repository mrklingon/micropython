# Imports go at the top
from microbit import *
import random
import time
import music
import speech
from stars import *





def blast(x):
    for i in range(5):
        if display.get_pixel(x,4-i) == 8:
            #Klingon!
            score = score + 1+ random.randrange(10)
            speech.say("Klingon!")
            music.BLUES
        display.set_pixel(x,4-i,9)

shipx = 2
shipy = 4
score = 0
for x in range(30):
    fnstarsS()
    fnslideS()
    time.sleep(.1)

for x in range(30):
    fnstarsS()
    fnslideS()
    time.sleep(.1)


for x in range(30):
    fnstarsE()
    fnslideE()
    time.sleep(.1)

for x in range(30):
    fnstarsW()
    fnslideW()
    time.sleep(.1)

while True:
    fnstars()
    fnslide()
    display.set_pixel(shipx,shipy,9)
    time.sleep(.2)
    
    if accelerometer.was_gesture('shake'):
       blast(shipx)
    
    if button_a.was_pressed() and button_b.was_pressed():
        blast(shipx)
    
    if button_a.is_pressed():
        shipx = shipx - 1
        if shipx < 0 :
            shipx=0
    if button_b.is_pressed():
       shipx = shipx + 1
       if shipx > 4 :
            shipx=4    
    
