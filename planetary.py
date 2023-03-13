# Imports go at the top
from microbit import *
import speech
import music
import random
import time

planets = ["Mercury","Venus","Earth","Mars","Ceres","Jupiter","Saturn","Uranus","Neptune","Pluto","Eris"]
year = [.24,.62,1,1.9,4.6,11.9,29.4,83.7,163.7,248,557]
day = [59,243,1,1.03,.38,.42,.44,.72,.72,.67,6.4,8]
planet = 0
curp = 10

info = False
# Code in a 'while True:' loop repeats forever
while True:
    if planet != curp:
        display.scroll(planets[planet][0])
        speech.say(planets[planet])
        curp = planet

    if (button_a.is_pressed() and button_b.is_pressed()) or accelerometer.was_gesture('shake') :
        if info:
            info = False
            speech.say("planet mode")

        else:
            info = True
            speech.say("info mode")
            
    if not info:
        if button_a.was_pressed():
                planet = planet + 1 
                if planet > 10:
                    planet = 0
        if button_b.was_pressed():
                planet = planet - 1
                if planet <0:
                    planet = 10
    else:
        if button_a.was_pressed():
            display.scroll(planets[planet][0])
            speech.say(planets[planet])
            
        if button_b.was_pressed():
           speech.say("year" + str(year[planet]))
           display.scroll(year[planet])
           speech.say("day "+str(day[planet]))
           display.scroll(day[planet])
    
    time.sleep(.25)
