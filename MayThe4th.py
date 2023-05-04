# Imports go at the top
from microbit import *
import speech
import random

ships = ["Kalee Bastion",
    "Gand Navigator",
    "Calamity",
    "Harmony",
    "Blade",
    "Beast",
    "Mandalorian Mercenary",
    "Naboo Brute",
    "Devaron Marauder",
    "Messenger"]
planets = ["Lelsodi",
    "Asem",
    "Chevu",
    "Russuc",
    "Okind",
    "Truth",
    "Tor",
    "Urre",
    "Vit",
    "Yus"]
jedi = ["Dansinc Romerai",
    "Calrya Popwadh",
    "Micdom Connbene",
    "Josbray Aswgrah",
    "Rylejov Cradeer",
    "Coopalfr Belcros",
    "Coleconn Haynnor",
    "Jortrav Plarode",
    "Giantyle Permilb",
    "Brygabr Vinerr"]
Travel = ["escapes from", "returns from ", "flies to"]

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image('00300:'
                       '03630:'
                       '36963:'
                       '03630:'
                       '00300'))

    if button_a.is_pressed():
        display.scroll('Jedi ',100)
        j = random.choice(jedi)
        display.scroll(j,100)
        speech.say('jedi '+ j)
    
    if button_b.is_pressed():
        j = random.choice(jedi)
        p = random.choice(planets)
        s = random.choice(ships)
        t = random.choice(Travel)
        speech.say('Jedi ' +j)
        display.scroll('Jedi '+j,60)
        speech.say(t)
        display.scroll(t,60)
        speech.say(p)
        display.scroll(p,60)
        speech.say(" using "+ s)
        display.scroll('using '+s,60)
