import time
import random
import speech
from microbit import *


races = ["human", "elf", "dwarf", "hobbit"]
classes = ["wizard", "burglar",  "healer", "warrior"]
names = [
    "Krargrouk Honorgrog",
    "Kargroun Shadowbrew",
    "Vomdoick Emberminer",
    "Polo Littlefoot",
    "Leutfrid Baggins",
    "Fastolph Gardner",
    "Alen Tormyar",
    "Ascal Perbanise",
    "Felaern Tortoris",
    "Crestiennet of the Night",
    "Thilrern Derorvo",
    "Bheksomu Dreinzul",
    "Khondui Bhugazel",
    "Averitt the Heroic",
    "Heimeri of the South",
]

destination = [
    "Alterwood Palace",
    "Corftey Fortress",
    "Clarn Castle",
    "Wringcaster Citadel",
    "The Eternal Haunt",
    "The Buried Burrows",
    "The Ethereal Cells  ",
    "Water Leopard Woods",
    "Baxpool Covert",
    "Kirkasing Woodland",
]

weapons = [
    "Soulsliver",
    "Cryptic",
    "Blackout",
    "Doomguard",
    "Windsong Idol",
    "Thirsting Slicer",
    "Isolated Copper Sabre",
    "Pride's Steel Protector",
    "Aetherius, Quickblade of Eternal Bloodlust",
    "Treachery, Spine of Justice",
    "Stinger, Claymore of the Burning Sun",
    "Barbarian Iron Deflector",
    "Mournblade, Gift of Ancient Power",
]

enemy = [
    "Phasething",
    "Chaosling",
    "Rottingstep",
    "Boulderfang",
    "Phantomman",
    "Dreadcrackle",
    "Soilserpent",
    "Mornlich",
    "The Lanky Statue",
    "The Feathered Bane Jackal",
    "The Black-Eyed Cinder Spider",
    "The Tusked Venom Drake",
]


travel = [" travels to", " returns from", " explores within", " gets lost at"]
treasure = [
    "Fortune's Horn",
    "Worship Mirror",
    "Insanity Boots",
    "Sanctifying Ark",
    "Roaring Scepter",
    "Misty Satchel",
    "Hailstorm Charm",
]

forest = [
    "Misty Bluff Wilds",
    "Pleasant Brook Grove",
    "Huge Wilds",
    "Majestic Wilds",
    "Short-Tailed Snail Woodland",
    "Speckled Squirrel Grove",
    "Faint Wood",
    "Jagged Covert",
    "Short-Tailed Treefrog Grove",
    "Imperial Spider Covert",
    "Mannear Wilds",
    "Shipsons Wood",
    "Alberboia Grove",
    "Bois de la Camris",
    "Fort du Bouluon",
    "Fort de la Carcaveil",
    "Fort de la Sarmont",
]

problem = [
    "Suddenly out of {frst} appears a {monster}",
    "{name} is surprised when {monster} attacks from {frst}",
    "A battle begins. The deadly {monster} attacks {name} after leaping out of {frst}!",
    "Alarm! {monster} materializes from the edge of {frst}!",
]

solution = [
    "Stumbling badly, {name} somehow manages to find the {weapon} and dispatch them!",
    "Heroicly, {name} quickly banishes the creature to {forest} with the {weapon}.",
    "Even though {name} fails to find a weapon like {weapon}, the monster shuffles away to {forest}",
]


purpose = ["seeking", "discovering", "losing", "finding"]


def player():
    nm = random.choice(names)
    rc = random.choice(races)
    cl = random.choice(classes)
    return [nm, rc, cl]


Done = False
Player = player()

ind = 0
while not Done:
    if button_a.was_pressed():
        Player = player()
        speech.say(("The " + Player[1] + " " + Player[2] + " " + Player[0]))

        display.scroll("name: "+Player[0])
        display.scroll("type: "+Player[1])
        display.scroll("class: "+Player[2])

        
        
    if button_b.was_pressed():
       speech.say(("The " + Player[1] + " " + Player[2] + " " + Player[0]))
        
       speech.say(random.choice(travel))
       speech.say(random.choice(destination))
       speech.say(random.choice(purpose) + " " + random.choice(treasure))
       
       solve = random.choice(problem).format(
                name=Player[0], frst=random.choice(forest), monster=random.choice(enemy)) 
       words = solve.split(" ")
       for word in words:
           speech.say(word)

       solve =  random.choice(solution).format(
                name=Player[0],
                forest=random.choice(forest),
                monster=random.choice(enemy),
                weapon=random.choice(weapons),
            )
       words = solve.split(" ")
       for word in words:
           speech.say(word)

   
