#While Loop Example
#By Matthew Brown, Bayside Secondary School


import sys                  #This is only used for the sys.exit() thing to end the program.
import random               #This is so we can use random number generation to get 3 diff. responses.
from time import sleep      #Used heavily for dramatic effect.

password = "Mayonnaise" #Pretty important. This is what the correct password is.

p = input("Enter the Password: ") #Gets the password attempt from the user.

global count
count = 1 #Defines that this is their first try.

global tries #Defines how many times you want to give the user before shutting down.
tries = 5   #This is good to have here so you can change it easily up here and not have to fiddle with several lines.


def response(): #This function makes it so that you can get up to 3 different responses.
    num = random.randint(1,3)

    if num == 1:
        print("Wrong password, stupid.")
    elif num == 2:
        print("You dun goofed. Great work.")
    elif num == 3:
        print("Great job! You failed. Go back to school.")


while (p != password): #Checks if the password they gave is incorrect: if it is, it runs this block of "check yourself" code.

    print("Checking...") ## Some visual aids to show it's checking, 
    sleep(0.25)          ## as well as a loading thing to give
    print("\n")          ## some 'tactile' feedback.

    if count < tries: #If they've tried less than the maximum number of attempts, it tells them and lets them try again.
        response()
        print("Try again.")
        print("\n")
        p = input()
        
        count = count + 1
        
    elif count >= tries:                    #However, if they've hit their maximum number of attempts, this runs instead:
        print("You tried too many times.")  # telling them to try again later and closing the program.
        print("Come back tomorrow.")
        sys.exit()
        
if p == password: #This if statement isn't really necessary, it's just a final safeguard of the program.
    print("Checking...")
    sleep(0.5)
    print("\n")
    sleep(2)
    print("Access granted.")
    
    print("You got it after %s failed attempts. You had a maximum of %s tries."%(count - 1, tries))
    print("\n")

    sleep(1.5)
    print("Here's the rest of the program!")
    sleep(1)
    print("\n")
    sleep(3)
    print("\n"*3)

elif p != password: #This should never run, unless they manage to bust past the while loop. 
    print("Checking...")
    sleep(0.5)
    print("\n")
    sleep(5)
    print("You broke past the while loop, but you can't get past here!")
    print("I don't even know how you got down to this point. If you did, congrats. You broke it.")
    
    sleep(0.5)
    sys.exit()

###################################################
##  Starts the program from yesterday :^)        ##
##  That way the password actually has a point.  ##
##  This was just kind of a silly extra bit.     ##
###################################################

def nameGet(): #Gets the name from the user
    global name
    name = input("Type your name, please: ")

def ageGet(): #Gets the user's age
    global age
    age = input("Type your age: ")

def nameRun(): #Runs through the name, checking if there are any numbers. If there are, it asks again.

    if name.isalpha() == True:
        sleep(0.1)
        print("%s, huh? That's a nice name."%(name))

    else:
        print("\n") #These make sure you can really see the denial the program feels.
        print("Type a real name! Don't use numbers.")
        nameGet()
        nameRun()

def ageRun(): #Does the same as nameRun(), but this time it checks if the age is in numbers.

    if age.isnumeric() == True:
        global agenum
        agenum = int(age)
        
        sleep(0.1)
        print("You're %s?"%(agenum))

    else:
        print("\n") #These make sure you can really see the denial the program feels.
        print("Please type a number!")
        ageGet()
        ageRun()

#Actual program begins. 

print("Hello!")
print("What is your name?")
print("\n")

nameGet() #Gets the name
sleep(0.5)
nameRun() #Checks the name, and gives a reply

sleep(1.5)

print("\n")
print("Okay, %s, how old are you?"%(name))
print("\n")

ageGet() #Gets the age
sleep(0.5)
ageRun() #Gets a short reply, followed by a longer one with some (extremely) basic math. VV Down Below VV

print("\n")
print("Okay, you'll be %s next year, then."%(agenum + 1))


##Unedited program from yesterday ends, this last line was added today.
sys.exit()
