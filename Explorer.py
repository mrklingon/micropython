from microbit import *
import random
import time
from stars import *
score = 0

joystick_x = pin1
joystick_y = pin2
button_c = pin12
button_d = pin13
button_e = pin14
button_f = pin15

shipx =2
shipy =2

dirs = ["w","n","s","e"]
dir = 0 

def btns():
    rv = -1
    if button_c.read_digital() == 0:
        print("c")
        return 0
    if button_d.read_digital() == 0:
        print("d")
        return 1
    if button_e.read_digital() == 0:
        print("e")
        return 2
    if button_f.read_digital() == 0:
        print("f")
        return 3 
    
    return rv
def mv(dr):
    if dr == 0:
        fnstarsE()
        fnslideE()
    if dr == 1:
        fnstars()
        fnslide()
    if dr == 2:
        fnstarsS()
        fnslideS()
    if dr == 3:
        fnstarsW()
        fnslideW()
while True:
        mv(dir)
        #nav = btns()
        #print(nav)
        
        #if nav != -1:
         #   dir = nav
        if button_a.was_pressed():
            blast(shipx,shipy,dir)
        time.sleep(.1)
        if button_b.was_pressed():
            bomb()
        x = joystick_x.read_analog()
        y = joystick_y.read_analog()
        display.set_pixel(shipx,shipy,9)
        time.sleep(.1)
        display.set_pixel(shipx,shipy,0)
        if y >550:
            shipy = shipy -1
            dir = 1
            if shipy<0:
                shipy = 0
        if y <400:
            shipy = shipy + 1
            dir = 2
            if shipy > 4:
                shipy = 4
        if x >550:
            shipx = shipx -1
            dir = 0
            if shipx<0:
                shipx = 0
        if x <500:
            shipx = shipx + 1
            dir = 3
            if shipx > 4:
                shipx = 4
