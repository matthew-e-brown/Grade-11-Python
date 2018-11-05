#Random Number Generation & Ranges
#Matthew Brown, Bayside Secondary

import sys
from random import *
from time import sleep

'''print("Testing Random Number Gen...")
sleep(0.75)
print (randint(0,100))

sleep(1)

print("\n\nTesting range of 0, 10... (multiplied by a randint)")

sleep(1)

for i in range(0,10):
    sleep(0.5)
    print(i*(randint(0,100)), end=" ")

sleep(1)

print("\n\nTesting range of 0, 11...")

sleep(1)

for i in range(0,11):
    sleep(0.125)
    print(i, end=" Ghosts ")

sleep(1)
print("\nHoly cow!! Sp0oOky! :O")
sleep(1)

print("\n\nTesting range of 0, 100, 3...")

sleep(1)

for i in range(0,100,3):
      sleep(0.05)
      print(i, end=" ")'''


print("\n"*3 + "Testing randints in loops w/ ranges")
sleep(1)

print("\nYour dice roll numbers are:\n")

for i in range(2):
    r = randint(1,6)
    print(r, end=" ")
