from microbit import *
import random
import time
import music


def universe():
    cosmos = []
    for x in range(20*20):
        if random.randrange(100)>37:
            cosmos.append(random.randrange(5)+1)
        else:
            cosmos.append(0)
    return (cosmos)

uni = universe()

def loc(x,y):
    return x+(y*20)

def point(x,y,cosmos):
    p = x + (y*20)
    return cosmos[p]
def show(xx,yy):
    for y in range(5):
        for x in range(5):
            display.set_pixel(x,y,point(xx+x,yy+y,uni))

def laser():
    for l in range(4):
        display.set_pixel(sx,l+1,9)
        uni[loc(x+sx,y+l)]=0
        time.sleep(.05)
    for l in range(4):
        display.set_pixel(sx,l+1,0)
        time.sleep(.05)

show(0,0)
x=7
y=0
sx = 2
while True:
   y = y+1
   if y>14:
       y=0
   show(x,y)
   if display.get_pixel(sx,0) == 5:
       music.play(music.BA_DING)
           
   display.set_pixel(sx,0,9)
   time.sleep(.2)
   if button_a.was_pressed():
       laser()
   if accelerometer.was_gesture('left'):
       sx = sx-1
       if sx <= 0:
           sx=0
           x = x-1
           if x<0:
               x=0
   if accelerometer.was_gesture('right'):
       sx = sx+1
       if sx >= 4:
           sx=4
           x = x+1
           if x>14:
               x=14
               
