from time import sleep

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
        print("\n")
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
        print("\n")
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
