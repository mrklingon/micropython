from microbit import *
import random

def fnstars():
    for i in range(5):
        if random.randrange(10)>8:
            display.set_pixel(i,0,1+random.randrange(6))
        else:
            display.set_pixel(i,0,0)


def fnslide():
    for i in range(4):
        for j in range(5):
            display.set_pixel(j,4-i,display.get_pixel(j,3-i))


def fnstarsS():
    for i in range(5):
        if random.randrange(10)>8:
            display.set_pixel(i,4,1+random.randrange(6))
        else:
            display.set_pixel(i,4,0)


def fnslideS():
    for i in range(4):
        for j in range(5):
            display.set_pixel(j,i,display.get_pixel(j,i+1))


def fnstarsE():
    for i in range(5):
        if random.randrange(10)>8:
            display.set_pixel(0,i,1+random.randrange(6))
        else:
            display.set_pixel(0,i,0)


def fnslideE():
    for i in range(4):
        for j in range(5):
            display.set_pixel(4-i,j,display.get_pixel(3-i,j))

def fnstarsW():
    for i in range(5):
        if random.randrange(10)>8:
            display.set_pixel(4,i,1+random.randrange(6))
        else:
            display.set_pixel(4,i,0)


def fnslideW():
    for i in range(4):
        for j in range(5):
            display.set_pixel(i,j,display.get_pixel(i+1,j))
