# Imports go at the top
from microbit import *
import random
import time
import music
import speech
from stars import *





def blast(x):
    global score
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

dirs = [0,1,2,3]
north = 0
east = 1
south = 2
west = 3

dir = north
motion = True


while True:
    if motion:
        if dir == north:
            shipx = 2
            shipy = 4
            fnstars()
            fnslide()
            display.set_pixel(shipx,shipy,9)
            time.sleep(.2)
    
        
        if dir == east:
            shipy = 2
            shipx = 4
            fnstarsE()
            fnslideE()
            display.set_pixel(shipx,shipy,9)
            time.sleep(.2)
    
        
        if dir == south:
            shipy = 0
            shipx = 2
            fnstarsS()
            fnslideS()
            display.set_pixel(shipx,shipy,9)
            time.sleep(.2)
    
           
        if dir == west:
            shipy = 2
            shipx = 0
            fnstarsW()
            fnslideW()
            display.set_pixel(shipx,shipy,9)
            time.sleep(.2)
     
   
    if (button_a.was_pressed() and button_b.was_pressed()) or accelerometer.was_gesture('shake'):
        if motion:
            motion = False
        else:
            motion = True
        

    
    if button_a.is_pressed():
       motion = True
       dir = dir+1
       if dir > 3:
           dir = 0
    
    if button_b.is_pressed():
       motion = True
       dir = dir-1
       if dir < 0:
           dir = 3
       
       
    
