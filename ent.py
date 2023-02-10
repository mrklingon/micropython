from microbit import *
import speech
import random
import music

star1 = Image("03020:"
"00300:"
"10000:"
"00300:"
"90001:"
)

star2 = Image("00300:"
"10000:"
"00300:"
"90001:"
"00000:"
)

star3 = Image("10000:"
"00300:"
"90001:"
"00000:"
"03000:"
)

star4 = Image("00300:"
"90001:"
"00000:"
"03000:"
"00000:"
)

star5 = Image("90001:"
"00000:"
"03000:"
"00000:"
"00030:"
)

star6 = Image("00000:"
"03000:"
"00000:"
"00030:"
"03090:"
)

star7 = Image("03000:"
"00000:"
"00030:"
"03090:"
"01000:"
)

star8 = Image("00000:"
"00030:"
"03090:"
"01000:"
"05030:"
)

star9 = Image("00030:"
"03090:"
"01000:"
"05030:"
"00300:"
)

star10 = Image("03090:"
"01000:"
"05030:"
"00300:"
"10050:"
)

star11 = Image("01000:"
"05030:"
"00300:"
"10050:"
"00030:"
)

star12 = Image("05030:"
"00300:"
"10050:"
"00030:"
"02000:"
)

star13 = Image("00300:"
"10050:"
"00030:"
"02000:"
"03020:"
)

star14 = Image("10050:"
"00030:"
"02000:"
"03020:"
"00300:"
)

star15 = Image("00030:"
"02000:"
"03020:"
"00300:"
"10000:"
)

star16 = Image("02000:"
"03020:"
"00300:"
"10000:"
"00300:"
)

star17 = Image("03020:"
"00300:"
"10000:"
"00300:"
"90001:"
)

star18 = Image("00300:"
"10000:"
"00300:"
"90001:"
"00000:"
)

star19 = Image("10000:"
"00300:"
"90001:"
"00000:"
"03000:"
)

star19 = Image("00300:"
"90001:"
"00000:"
"03000:"
"00000:"
)

star20 = Image("90001:"
"00000:"
"03000:"
"00000:"
"00030:"
)

star21 = Image("00000:"
"03000:"
"00000:"
"00030:"
"03090:"
)

star22 = Image("03000:"
"00000:"
"00030:"
"03090:"
"01000:"
)

star23 = Image("00000:"
"00030:"
"03090:"
"01000:"
"05030:"
)

star24 = Image("00030:"
"03090:"
"01000:"
"05030:"
"00300:"
)

star25 = Image("03090:"
"01000:"
"05030:"
"00300:"
"10050:"
)

star26 = Image("01000:"
"05030:"
"00300:"
"10050:"
"00030:"
)

star27 = Image("05030:"
"00300:"
"10050:"
"00030:"
"02000:"
)

ALLSTARS = [star1, star2, star3, star4, star5, star6, star7, star8,
            star9, star10, star11, star12, star13, star14, star15,
            star16, star17, star18, star19, star20, star21, star22,
            star21, star23, star24, star25, star26, star27]



RALLSTARS =[star27, star26, star25, star24, star23, star22, star21, star20,
            star19, star18, star17, star16, star15, star14, star13, star12,
            star11, star10, star9, star8, star7, star6, star5, star4, star3,
            star2, star1]


ent1 = Image("99900:"
           "09099:"
           "09990:"
           "00000:"
           "00000:")

ent2 = Image("99000:"
           "90990:"
           "99900:"
           "00000:"
           "00000:")

ent3 = Image("90000:"
           "09900:"
           "99000:"
           "00000:"
           "00000:")

ent4 = Image("00000:"
           "99000:"
           "90000:"
           "00000:"
           "00000:")


ent5 = Image("00000:"
           "90000:"
           "00000:"
           "00000:"
           "00000:")

ent6 = Image("00000:"
           "00000:"
           "00000:"
           "00000:"
           "00000:")

ALLENT = [ent1, ent2, ent3, ent4, ent5, ent6]

pointx = 2
pointy = 2

display.show(ALLENT)

display.show(RALLSTARS,wait=False,loop=True,delay=150)

Game = True

while Game:
    if  button_a.was_pressed():
        pointx = pointx - 1
        if pointx < 0:
            pointx = 0

    if button_b.was_pressed():
        pointx = pointx + 1
        if pointx > 4:
            pointx = 4

    if accelerometer.was_gesture("up"):
        pointy = pointy - 1
        if pointy < 0:
            pointy = 0

    if accelerometer.was_gesture("down"):
        pointy = pointy + 1
        if pointy > 4:
            pointy = 4


    if display.get_pixel(pointx, pointy) == 9:
        #a ship - go BOOM
        Game = False
    display.set_pixel(pointx,pointy,8)

music.play(music.FUNK)
display.scroll("KA-BOOOM!")



display.show(ALLENT)

display.show(ALLSTARS,wait=False,loop=True,delay=150)

Game = True

while Game:
    if  button_a.was_pressed():
        pointx = pointx - 1
        if pointx < 0:
            pointx = 0

    if  button_b.was_pressed():
        pointx = pointx + 1
        if pointx > 4:
            pointx = 4

    if accelerometer.was_gesture("up"):
        pointy = pointy - 1
        if pointy < 0:
            pointy = 0

    if accelerometer.was_gesture("down"):
        pointy = pointy + 1
        if pointy > 4:
            pointy = 4


    if display.get_pixel(pointx, pointy) == 9:
        #a ship - go BOOM
        Game = False
    display.set_pixel(pointx,pointy,8)

music.play(music.FUNERAL)

display.scroll("Game OVER!! KA-BOOOM!")



