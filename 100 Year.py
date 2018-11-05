from time import sleep
from datetime import datetime

curDT = datetime.now()
curYR = str(curDT)[0:4]

nameIN = input("Tell me your name: ")

while nameIN.isalpha() != True:
    nameIN = input("\nPlease use letters only. Try again: ")

sleep(1)
print("\nOkay, %s, you've got a nice name."%(nameIN))
sleep(0.8)
print("Alright, now how old are you?")

sleep(0.5)
ageIN = input("\nTell me your age: ")

while ageIN.isnumeric() != True:
    ageIN = input("\nPlease use numbers only. Try again: ")

sleep(1)

print("\nSounds good. Your name is %s and you are %s years old."%(nameIN, ageIN))

bthYR = int(curYR) - int(ageIN)
hndYR = bthYR + 100

print("Hey, have you had a birthday yet this year? This will help me determine your birth year.")
print("Just type \"Yes\" or \"No\". Exactly like that.")

bDay = input("\nHave you? :: ")

if str(bDay) == "Yes":
    print("\nJust for fun, I figured out that, in %s, you'll turn 100."%(hndYR))
    
elif str(bDay) == "No":
    print("\nJust for fun, I figured out that, in %s, you'll turn 100."%(hndYR-1))
    
else:
    while str(bDay) != "Yes" or str(bDay) != "No":
        print("Use \"Yes\" or \"No\". Nothing else.")
        bDay = input("\nHave you? :: ")
        
    if str(bDay) == "Yes":
        print("\nJust for fun, I figured out that, in %s, you'll turn 100."%(hndYR))
    elif str(bDay) == "No":
        print("\nJust for fun, I figured out that, in %s, you'll turn 100."%(hndYR-1))



