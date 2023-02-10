# Write your code here :-)
from microbit import *
import speech
import random
from microbit import sleep

nlist = ["yawne", "kaltxi", "tawsip", "'eylan", "kelku", "safla", "tiyora'", "'itan", "'ite", "'ipu", "uvan", "syure", "yom"]
mlist = ["cyare", "Sucuy'gar", "me'sen", "burc'ya", "yaim", "bralov", "parjai", "ad", "ad", "nuh'la", "geroya", "kai'tome", "epar"]
klist = ["bang", "nuqneH", "'ejDo'", "jup ", "juH", "Qapla'", "yay", "puqloD", "puqbe'", "tlhaq", "Quj", "Soj", "Sop"]
elist = ["beloved", "hello", "starship", "friend", "home", "success", "victory", "son", "daughter", "funny", "game", "food", "eat"]

lang = 0
#  Klingon 0, Mando'a 1, Navi' 2

def clock():
    display.show(Image.ALL_CLOCKS)

def comp():
    display.show(Image.ALL_ARROWS)
word = random.randrange(0,len(nlist)-1)


for a in [1, 2, 3, 4]:
    display.show(Image.HEART, delay=400, wait=True)
    sleep(400)
    display.show(Image.HEART_SMALL, delay=400, wait=True)
    sleep(400)

while True:
    if (pin0.is_touched()):
        display.scroll(elist[word])

    if button_a.is_pressed():
        lang = lang + 1
        if (lang >2):
            lang = 0

        if (lang == 0):
            display.scroll("K")


        if (lang == 1):
            display.scroll("M")

        if (lang == 2):
            display.scroll("N")

    if button_b.is_pressed():
        word = random.randrange(0,len(nlist)-1)

        if (lang == 0):
            display.scroll((klist[word]))

        if (lang == 1):
            display.scroll((mlist[word]))

        if (lang == 2):
            display.scroll((nlist[word]))
#    if (accelerometer.current_gesture() == "shake"):