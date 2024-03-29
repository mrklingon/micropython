from microbit import *
import random
import time

debug = True
def outPut(txt):
    display.scroll(txt)
    print(txt)
    
def setWookie():
    outPut("Wookie")
    global vowels
    global consonants
    global rules

    vowels = "OUA"
    consonants = "WWRRRHHHWWWRR"
    rules = ["CvvvvC", "CVC", "VVCV", "VCVVVVC","VCVVC"]

def setKlin():
    outPut("Klingon")
    global vowels
    global consonants
    global rules

    vowels = "aeIouy"
    consonants = "bcDgHjlmnpqQStvwy'"
    rules = ["CVVC", "CVC", "CCVVC", "CVVC","CV"]

def setVul():
    outPut("Vulcan")
    global vowels
    global consonants
    global rules

    vowels = "'iaei'uaiyaoia"
    consonants = "whltrkltkt'khthtrvttsnzh"
    rules = ["CVcvcv", "Cvcv", "Ccv", "Cvvcv","CvVccvcv"]


def setMando():
    outPut("Mando'a")
    global vowels
    global consonants
    global rules

    vowels = "ouaaoaaaaeaeeeauiueaaeaeeaeoaeeaoaeooeaeaaeaeeeaeueeaieaaaoeeieiioaiaiaiae"
    consonants = "slstryshlntryshlntddthnhntcrcrtryshshtryshlnsh'''''''rslrl't'tdtd'tsh'hnshhn'tsh'cshk'tlsr'chkrvrrsrmsrmrdsnrrnrnrmjycrmjyc"

    rules = ["Cvvc", "CvCvC", "vCCvc", "cvVvCv","cvCCvc"]

def setRom():
    outPut("Romulan")
    global vowels
    global consonants
    global rules

    vowels = "'eiueeeiia''"
    consonants = "skfhvhlnvhdhmnhl'rh"

    rules = ["cvCCv", "cvVCv", "cVvCC", "cvVvCv","cVvCCv"]


def mkword():
    global lang
    rule = rules[random.randrange(len(rules))]
    if debug: print(rule)
    word = ""
    for i in range(len(rule)):
        r=rule[i]
        if debug: print(rule[i])
        if r == "V":
            word = word + pickChar(vowels)
        if r == "v":
            if (random.randrange(100)>49):
                word = word + pickChar(vowels)
        if r == "C":
            con = pickChar(consonants)
            if (con == "g" and lang == 2):
                con = "gh"
            word = word + con
        if r == "c":
            if (random.randrange(100)>49):
                con = pickChar(consonants)
                if (con == "g" and lang == 2):
                    con = "gh"
                word = word + con
 
    return word

def pickChar(inp):
    return (inp[random.randrange(len(inp))])

def mkPhrase():
    sent = ""
    for i in range(random.randrange(10)+1):
        sent = sent + " " + mkword()
    return sent


setWookie()

lang = 1
done = False

while True:
    if button_a.was_pressed():
    
      lang = lang + 1

    
      if lang > 5:
           lang = 1
    
      if lang == 1:
        setWookie()

      if lang == 2:
        setKlin()

      if lang == 3:
        setVul()

      if lang == 4:
        setMando()

      if lang == 5:
        setRom()

    time.sleep(.25)
    
    if button_b.was_pressed():
        outPut(mkword())

    
        
