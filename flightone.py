# Imports go at the top
from microbit import *
import random
import time
import music
import speech
from stars import *
while True:
    lives = 3
    
    shipx = 2
    shipy = 4
    score = 0
    
    
    dirs = [0,1,2,3]
    north = 0
    east = 1
    south = 2
    west = 3
    
    dir = north
    
    while lives > 0:
        score = score + 1    
        fnstars()
        fnslide()
        if display.get_pixel(shipx,shipy) != 0:
            music.play(music.BA_DING)
            lives = lives - 1
        display.set_pixel(shipx,shipy,9)
        time.sleep(.2)
        
        if accelerometer.was_gesture('shake') or pin1.is_touched():
            blast(shipx,shipy,dir)
    
        if button_a.is_pressed() and button_b.is_pressed():
            blast(shipx,shipy,dir)
        else:
            if button_a.is_pressed():
              shipx = shipx - 1
              if shipx < 0:
                  shipx = 0
            
            if button_b.is_pressed():
               shipx = shipx + 1
               if shipx > 4:
                   shipx=4
               
    display.show(Image.SKULL)
    music.play(music.FUNERAL)
    display.scroll(str(score))
    music.play(music.DADADADUM)
    time.sleep(1)
    wait = True
    while wait:
        display.show(Image.SQUARE)
        time.sleep(.5)
        display.show(Image.SQUARE_SMALL)
        time.sleep(.5)

        if button_a.is_pressed()or button_b.is_pressed():
            wait = False
                    
        
