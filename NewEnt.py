# Imports go at the top
from microbit import *
import random
import time

def fnstars():
    for i in range(5):
        if random.randrange(10)>8:
            display.set_pixel(i,0,1+random.randrange(7))
        else:
            display.set_pixel(i,0,0)


def fnslide():
    for i in range(4):
        for j in range(5):
            display.set_pixel(j,4-i,display.get_pixel(j,3-i))


def blast(x):
    for i in range(5):
        display.set_pixel(x,4-i,9)

shipx = 2
shipy = 4
while True:
    fnstars()
    fnslide()
    display.set_pixel(shipx,shipy,9)
    time.sleep(.2)
    
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
    
