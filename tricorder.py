from microbit import *
import speech
import random

#modes
modes = ["compass", "light", "temp", "uta", "enterprise"]

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


#FOR languages
nlist = ["yawne", "kaltxi", "tawsip", "'eylan", "kelku", "safla", "tiyora'", "'itan", "'ite", "'ipu", "uvan", "syure", "yom"]
mlist = ["cyare", "Sucuy'gar", "me'sen", "burc'ya", "yaim", "bralov", "parjai", "ad", "ad", "nuh'la", "geroya", "kai'tome", "epar"]
klist = ["bang", "nuqneH", "'ejDo'", "jup ", "juH", "Qapla'", "yay", "puqloD", "puqbe'", "tlhaq", "Quj", "Soj", "Sop"]
elist = ["beloved", "hello", "starship", "friend", "home", "success", "victory", "son", "daughter", "funny", "game", "food", "eat"]
langs = ["Klingon", "Mando'a", "Navi"]
lang = 0



def comp():
    cdeg = compass.heading()
    cphd = int((cdeg/90)+.5)
    display.scroll(str(cphd))
    speech.say("compass")
    speech.say(str(cphd))

def temp():
    tmp = 32 + ((9 * temperature())/5)
    display.scroll(str(tmp))
    speech.say("temp")
    speech.say(str(tmp))

def lite():
    light = display.read_light_level()
    display.scroll(str(light))
    speech.say("light")
    speech.say(str(light))

def uta():
    lang = random.randrange(3)  #pick language - Klingon/Mando'a/Navi
    word = random.randrange(len(nlist))
    display.scroll(langs[lang])
    speech.say(langs[lang])
    display.scroll(elist[word])
    speech.say(elist[word])
    if (lang == 0):
        display.scroll(klist[word])
        speech.say(klist[word])

    if (lang == 1):
        display.scroll(mlist[word])
        speech.say(mlist[word])

    if (lang == 2):
        display.scroll(nlist[word])
        speech.say(nlist[word])



#happy start
for a in [1, 2, 4]:
    display.show(Image.HEART, delay=400, wait=True)
    sleep(400)
    display.show(Image.HEART_SMALL, delay=400, wait=True)
    sleep(400)
    display.show(ALLENT)

speech.say("Hello there")
speech.say("nookneck")

display.show(Image.HEART)
display.scroll("tricorder")
speech.say("tricorder")

mode = 0 # 0 compass, 1 light, 2 temp, 3 uta, 4 enterprise

#dispatch loop
while True:
    if button_a.is_pressed():
        mode = mode + 1
        if (mode > 4):
            mode = 0

        display.scroll(modes[mode])
        speech.say(modes[mode])

    if button_b.is_pressed():
        if mode == 0:
            comp()

        if mode == 1:
            lite()

        if mode == 2:
            temp()

        if mode == 3:
            uta()

        if mode == 4:
            display.show(ALLENT)

