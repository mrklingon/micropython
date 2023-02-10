from microbit import *
import random
import music
import speech


state = 0
spoke = False

states = ["idle", "greeting", "happy", "sad", "farewell"]

words = ["", "nook-neck", "good! mahj-kah!", "jih-shock", "kah-plah"]


GREET = Image("90909:"
"90909:"
"99909:"
"90909:"
"00000:"
)

BYE = Image("00999:"
"00999:"
"90999:"
"09999:"
"00000:")

images = [Image.HEART, GREET ,Image.HAPPY, Image.SAD, BYE ]

while True:
    if accelerometer.was_gesture('left'):
        state=1 # greeting
        spoke = False
    if accelerometer.was_gesture('right'):
        state=4 # Bye
        spoke = False
    if button_b.is_pressed():
        state=3 # sad
        display.show(images[state])
        music.play(music.FUNERAL)
        spoke = False
    if button_a.is_pressed():
        state=2 # happy
        display.show(images[state])

        music.play(music.ENTERTAINER)
        spoke = False
    if accelerometer.was_gesture('shake'):
        state=0 # idle
        spoke = True

    display.show(images[state])

    if spoke == False:
        speech.say(words[state])
        spoke = True