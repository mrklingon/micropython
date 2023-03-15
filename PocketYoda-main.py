from microbit import *
import speech
import random
import music

yoda = [
    "Size matters not. Look at me.",
    "Fear is the path to the dark side. ",
    "Fear leads to anger. Anger leads to hate.",
    "Hate leads to suffering.",
    "Always pass on what you have learned."
    "luminous beings are we, not this crude matter.",
    "You will find only what you bring in.",
    "Control, control, you must learn control!",
    "In the end, cowards are those who follow the dark side.",
    "Difficult to see. Always in motion is the future.",
    "Many of the truths that we cling to depend on our point of view.",
    "Named must your fear be before banish it you can.",
    "You will know (the good from the bad) when you are calm, at peace.",
    "A Jedi uses the Force for knowledge and defense.",
    "Smaller in number are we, but larger in mind.",
    "Your path you must decide.",
    "Happens to every guy sometimes this does",
    "Adventure. Excitement. A Jedi craves not these things.",
]


y1 = Image('00000:'
      '99000:'
      '09000:'
      '09000:'
      '99900')

y2 = Image('00000:'
      '09900:'
      '00900:'
      '00900:'
      '09990')

y3 = Image('00000:'
      '00990:'
      '00090:'
      '00090:'
      '00999')

y4 = Image('00000:'
      '00900:'
      '09990:'
      '00900:'
      '09990')

yodas = [y1,y2,y3,y4]

display.show(yodas)

def ywsay():
    display.show(Image.HEART)
    word = random.randrange(len(yoda))
    words = yoda[word].split()
    for w in words:
        speech.say(w)
    display.scroll(yoda[word], 75, wait=False, loop=True)


def ysay():
    display.show(Image.HEART_SMALL)
    word = random.randrange(len(yoda))
    words = yoda[word].split()
    for w in words:
        speech.say(w)
    display.show(Image.HEART, clear=True)


First = True

while True:
    if accelerometer.was_gesture("shake"):
        music.play(music.POWER_UP)

    if accelerometer.was_gesture("left"):
        speech.say("left")
    if accelerometer.was_gesture("right"):
        speech.say("righ")
    if First:
        music.play(music.POWER_UP)
        First = False

    if button_a.is_pressed():
        ysay()
        display.show(Image('00000:'
          '90009:'
          '04940:'
          '99999:'
          '09990'))

    if button_b.is_pressed():
        ywsay()
