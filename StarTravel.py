# Imports go at the top
from microbit import *
from universe import *
import time
diam = 30
initUni(diam)

for x in range(diam-5):
    showxy(x,x)
    time.sleep(.33)

# Code in a 'while True:' loop repeats forever
while True:
   for y in range(diam-5):
       for x in range(diam-5):
           showxy(x,y)
           time.sleep(.25)
