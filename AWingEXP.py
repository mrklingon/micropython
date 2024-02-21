from microbit import *
import random
import time
import music
global score

def universe():
    cosmos = []
    for x in range(20*20):
        if random.randrange(100)>37:
            cosmos.append(random.randrange(5)+1)
        else:
            cosmos.append(0)
    return (cosmos)


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
    global score
    for l in range(4):
        display.set_pixel(sx,l+1,9)
        score = score + uni[loc(x+sx,y+l)]
        uni[loc(x+sx,y+l)]=0
        time.sleep(.05)
    for l in range(4):
        display.set_pixel(sx,l+1,0)
        time.sleep(.05)


display.show(Image('08080:'
                   '08480:'
                   '84448:'
                   '88088:'
                   '88888:'
                  ))
time.sleep(1)
display.scroll('A-Wing Explorer',90)

while True:
    uni = universe()
    x=7
    y=0
    show(x,y)
    sx = 2
    display.set_pixel(sx,0,9)
    score = 0
    lives = 5
    while lives>0:
       y = y+1
       if y>14:
           y=0
       show(x,y)
       if display.get_pixel(sx,0) == 5:
           lives = lives - 1
           print (lives)
           music.play(music.BA_DING)
               
       display.set_pixel(sx,0,9)
       time.sleep(.2)
       if button_a.was_pressed():
           laser()
       if button_b.was_pressed():
           #hyperspace
           for h in range(3):
                display.show(Image.DIAMOND_SMALL)
                time.sleep(.1)
                display.show(Image.DIAMOND)
                time.sleep(.1)
           uni = universe()
           x=7
           y=0
           show(x,y)
           sx = 2
           display.set_pixel(sx,0,9)
        #navigation
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
    #out of lives
    print ("game over")
    print ("score: "+str(score))
    display.show(Image.SKULL)
    time.sleep(.25)
    display.scroll("Game Over")  
    display.scroll("Score: "+ str(score))
    #pause / till press A to restart.
    while not button_a.was_pressed():
        display.scroll("Score: "+ str(score))
    
