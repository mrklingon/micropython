
from microbit import *

lnd1 = Image("00000:"
             "00033:"
             "00009:"
             "09990:"
             "90000:")

lnd2 = Image("00000:"
             "00333:"
             "00090:"
             "99909:"
             "00000:")

lnd3= Image("00000:"
            "03330:"
            "00900:"
            "99090:"
            "00009:")

lnd4= Image("00000:"
            "33300:"
            "09000:"
            "90909:"
            "00090:")

lnd5= Image("00000:"
            "33005:"
            "90009:"
            "09090:"
            "00900:")

lnd6= Image("00000:"
            "30055:"
            "00099:"
            "90900:"
            "09000:")

lnd7= Image("00000:"
            "00550:"
            "00990:"
            "09000:"
            "90000:")

lnd8= Image("00000:"
            "05500:"
            "09909:"
            "90000:"
            "00000:")

lnd9= Image("00000:"
            "55000:"
            "99090:"
            "00009:"
            "00000:")

lnd10 = Image("00000:"
              "00000:"
              "00900:"
              "00090:"
              "00009:")

lnd11 = Image("00000:"
              "00000:"
              "09000:"
              "00900:"
              "00099:")

lnd12 = Image("00000:"
              "00000:"
              "90000:"
              "09000:"
              "00999:")

lnd13 = Image("00000:"
              "00000:"
              "00000:"
              "90009:"
              "09990:")

lnd14 = Image("00000:"
              "00000:"
              "00009:"
              "00090:"
              "99900:")

lnd15 = Image("00000:"
              "00009:"
              "00090:"
              "00900:"
              "99000:")

lnd16 = Image("00000:"
              "00090:"
              "00909:"
              "09000:"
              "90000:")

lnd17 = Image("00000:"
              "00900:"
              "09090:"
              "90009:"
              "00000:")

lnd18 = Image("00000:"
              "09000:"
              "90900:"
              "00090:"
              "00009:")

lnd19 = Image("00000:"
              "90000:"
              "09000:"
              "00909:"
              "00090:")

lnd20 = Image("00000:"
              "00000:"
              "90000:"
              "09099:"
              "00900:")

lnd21 = Image("00000:"
              "00000:"
              "00000:"
              "90999:"
              "09000:")

lnd22 = Image("00000:"
              "00000:"
              "00000:"
              "09999:"
              "90000:")

lnd23 = Image("00000:"
              "00000:"
              "00000:"
              "99999:"
              "00000:")

lnd24 = Image("00003:"
              "00000:"
              "00009:"
              "99990:"
              "00000:")

lnd25 = Image("00033:"
              "00000:"
              "00099:"
              "99900:"
              "00000:")

lnd26 = Image("00333:"
              "00000:"
              "00999:"
              "99000:"
              "00000:")

lnd27 = Image("03330:"
              "00000:"
              "09999:"
              "90000:"
              "00000:")

lnd28 = Image("33300:"
              "00000:"
              "99999:"
              "00000:"
              "00000:")

lnd29 = Image("33000:"
              "00000:"
              "99990:"
              "00009:"
              "00000:")

lnd30 = Image("30000:"
              "00000:"
              "99900:"
              "00099:"
              "00000:")

lnd31 = Image("00000:"
              "00000:"
              "99000:"
              "00999:"
              "00000:")

lnd32 = Image("00000:"
              "00000:"
              "90000:"
              "09990:"
              "00009:")

lnd33 = Image("00000:"
              "00002:"
              "00000:"
              "99900:"
              "00099:")

lnd34 = Image("00000:"
              "00022:"
              "00000:"
              "99000:"
              "00999:")

lnd35 = Image("00000:"
              "00222:"
              "00000:"
              "90000:"
              "09999:")

lnd36 = Image("00000:"
              "02220:"
              "00000:"
              "00000:"
              "99999:")

lnd37= Image("00000:"
             "22200:"
             "00000:"
             "00009:"
             "99990:")

lnd38= Image("00000:"
             "22000:"
             "00000:"
             "00099:"
             "99900:")

lnd39= Image("00000:"
             "20000:"
             "00000:"
             "00999:"
             "99000:")

lnd40= Image("00000:"
             "00000:"
             "00000:"
             "09990:"
             "90009:")

lnd41=Image("00000:"
            "00000:"
            "00000:"
            "99900:"
            "00099:")

lnd42= Image("00000:"
             "00000:"
             "00000:"
             "99009:"
             "00990:")

lnd43 = Image("00000:"
              "00000:"
              "00000:"
              "90099:"
              "09900:")

lnd44 = Image("00000:"
              "00000:"
              "00009:"
              "00990:"
              "99000:")

lnd45 = Image("00000:"
              "00009:"
              "00099:"
              "09900:"
              "90000:")

lnd46 = Image("00000:"
              "00090:"
              "00999:"
              "99000:"
              "00000:")



ALL_LAND = [lnd1, lnd2, lnd3, lnd4, lnd5, lnd6, lnd7, lnd8, lnd9, lnd10, lnd11,
            lnd12, lnd13, lnd14, lnd15, lnd16, lnd17, lnd18, lnd19, lnd20, lnd21,
            lnd22, lnd23, lnd24, lnd25, lnd26, lnd27, lnd28, lnd29, lnd30, lnd31,
            lnd32, lnd33, lnd34, lnd35, lnd36, lnd37, lnd38, lnd39, lnd40, lnd41,
            lnd42, lnd43, lnd44, lnd45, lnd46]



Score = 0
pointx = 0
pointy = 0

def showXW(x,y):
    display.set_pixel(x,y,8)
    display.set_pixel(x+1,y,8)

display.show(ALL_LAND,wait=False,loop=True,delay=150)

Game = True
Shields = 3

while Game:
    if button_a.was_pressed():
        pointy = pointy  - 1
        if pointy < 0:
            pointy = 0

    if button_b.was_pressed():
        pointy = pointy + 1
        if pointy > 4:
            pointy = 4
    showXW(pointx,pointy)


    if display.get_pixel(pointx+2,pointy) == 5:
        pointx = 0
        pointy = 0
        Shields = Shields +1
        display.show(Image.DIAMOND,delay=1500)
        Score = Score + 100
        display.show(str(Shields),delay=1000)
        sleep(1000)
        display.show(ALL_LAND,wait=False,loop=True,delay=150)


    if display.get_pixel(pointx+2,pointy) == 9:
        Shields = Shields - 1
        display.show(Image.SKULL,delay=1000)
        sleep(1000)
        display.show(str(Shields),delay=1000)
        sleep(1000)
        pointx = 0
        pointy = 0

        display.show(ALL_LAND,wait=False,loop=True,delay=150)
        if Shields == 0:
            Game = False


display.scroll("KA-BOOM! Game Over!")
display.scroll("score:")
display.scroll(Score)
