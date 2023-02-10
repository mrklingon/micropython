from microbit import *
import music

while True:
    tone=accelerometer.get_y()
    if tone>0:
        music.pitch( tone, 10)