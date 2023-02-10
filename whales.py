from microbit import *
import utime
import random
import music
import speech

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")
boat1 = Image("05050:"
              "05050:"
              "99999:"
              "09990:"
              "00000")

boat2 = Image("05050:"
              "99999:"
              "09990:"
              "00000:"
              "00000")

boat3 = Image(
             "99999:"
             "09990:"
             "00000:"
             "00000:"
             "00000")
boat4 = Image(
             "09990:"
             "00000:"
             "00000:"
             "00000:"
             "00000")

xboat1 = Image("00000:"
             "05050:"
             "05050:"
             "05050:"
             "99999"
             )

xboat2 = Image("00000:"
             "00000:"
             "05050:"
             "05050:"
             "05050"
                          )

xboat3 = Image("00000:"
             "00000:"
             "00000:"
             "05050:"
             "05050"
                          )

xboat4 = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "05050:"
                          )

BOATS= [boat,boat1,boat2,boat3,boat4]
XBOATS = [boat,xboat1,xboat2,xboat3,xboat4]
display.show(boat)

whale = Image("00099:"
              "00969:"
              "096690:"
              "00900:"
              "00990:")


whale1 = Image("09900:"
              "09690:"
              "96690:"
              "00900:"
              "09900:")

whale2 = Image("99000:"
              "09690:"
              "96690:"
              "00900:"
              "00990:")

WHALES = [whale,whale1,whale2,whale1,whale]

display.show(WHALES)
display.show(boat)
utime.sleep(2)
display.show(BOATS)

Game = True
Shields = 3
speech.say("Ahoy, it's time for the whales to get their revenge!")

def spotx(spot):
    sx = spot - (5 * int(spot/5))
    return sx

def spoty(spot):
    sy = int(spot/5)
    return sy

def limit(spot):
    if (spot>24):
        spot=spot-24

    if (spot<0):
        spot=spot+24

    return spot

def whaleclear(spot):
    display.set_pixel(spotx(spot),spoty(spot),0)

def whalemove(spot,delta):
    display.set_pixel(spotx(spot),spoty(spot),0)
    spot = limit(spot+delta)
    display.set_pixel(spotx(spot),spoty(spot),9)
    utime.sleep_ms(300)
    display.set_pixel(spotx(spot),spoty(spot),3)
    utime.sleep_ms(300)
    display.set_pixel(spotx(spot),spoty(spot),7)

    return spot

whale1 =17
whale2 =8
whale3 = 20

while Game:
        move = random.randint(-6,6)
        whale1=whalemove(whale1,move)
        move = random.randint(-6,6)
        whale2=whalemove(whale2,move)
        utime.sleep_ms(500)
        move = random.randint(-6,6)
        whale3=whalemove(whale3,move)

        if (whale1 == 1) or (whale2 == 1) or (whale3 == 1):
            Shields = Shields -1

        if (whale1 == 2) or (whale2 == 2) or (whale3 == 2):
            Shields = Shields -1

        if (whale1 == 3) or (whale2 == 3) or (whale3 == 3):
            Shields = Shields -1

        if (Shields < 1) :
            Game = False

whaleclear(whale1)
whaleclear(whale2)
whaleclear(whale3)

speech.say("The whales win!")
display.scroll("Hooray, the whales sunk the ship!!",delay=75)
music.play(music.FUNERAL)

