# Imports go at the top
from microbit import *
import time
import random

nlist = ["yawne",
    "kaltxi",
    "tawsip",
    "'eylan",
    "kelku",
    "safla",
    "tiyora'",
    "'itan",
    "'ite",
    "'ipu",
    "uvan",
    "syure",
    "yom"]
mlist = ["cyare",
    "Sucuy'gar",
    "me'sen",
    "burc'ya",
    "yaim",
    "bralov",
    "parjai",
    "ad",
    "ad",
    "nuh'la",
    "geroya",
    "kai'tome",
    "epar"]
klist = ["bang",
    "nuqneH",
    "'ejDo'",
    "jup ",
    "juH",
    "Qapla'",
    "yay",
    "puqloD",
    "puqbe'",
    "tlhaq",
    "Quj",
    "Soj",
    "Sop"]
elist = ["beloved",
    "hello",
    "starship",
    "friend",
    "home",
    "success",
    "victory",
    "son",
    "daughter",
    "funny",
    "game",
    "food",
    "eat"]
klingon = 0
mandoa = 1
navi = 2
langs = ["K","M","N"]
word = 0

lang = klingon

# Code in a 'while True:' loop repeats forever
for r in range(4):
    display.show(Image.DIAMOND)
    time.sleep(.2)
    display.show(Image.DIAMOND_SMALL)
    time.sleep(.2)
    display.clear()
display.show(langs[lang])
time.sleep(.5)
display.clear()
while True:
    v = 0
    output = ""
    if button_a.was_pressed():
        v = v+1
        time.sleep(.5)
        display.clear
    if button_b.was_pressed():
        v= v+2

    if v == 1: #advance language
        lang = lang+1
        if lang > 2:
            lang = 0
        display.show(langs[lang])
        time.sleep(.5)
        display.clear()
 
    if v ==2: #display current word
        if lang == klingon:
            display.scroll(klist[word])
        if lang == mandoa:
            display.scroll(mlist[word])
        if lang == navi:
            display.scroll(nlist[word])
        display.scroll("/"+elist[word])
        time.sleep(.5)
        display.clear()
    if v ==3: #display language
        display.show(langs[lang])
        time.sleep(.5)
        display.clear()
        
    if accelerometer.was_gesture('left'):
        word = word - 1
        if word<0:
            word = len(elist)-1
            display.clear()
        display.scroll(elist[word])
        time.sleep(.5)
    if accelerometer.was_gesture('right'):
        word = word + 1
        if word>len(elist)-1:
            word = 0
            display.clear()
        display.scroll(elist[word])
        time.sleep(.5)
    
        
        
