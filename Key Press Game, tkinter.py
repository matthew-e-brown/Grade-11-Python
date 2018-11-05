## MODIFIED FILE, TRYING TO USE TKINTER


##  ---------------------------------------------  ##

##  KeyPress Game,
##  M. Brown, ISC201, March 22nd, 23rd, 2017.

##  Desc.
##  
##  User will be prompted with a character.
##  the user must type and enter that character
##  as fast as they can.
##  
##  By default, the user can make five
##  mistakes before the game is over,
##  and they have 30 seconds. Each letter they
##  get correct will add 0.5 second to their time,
##  so if they go faster than 2/second they can go
##  forever, or until they lose steam.
##  These values can be changed by modifying
##  the global variables "timer" and "mistakes".

##  ---------------------------------------------  ##

import random, time
from tkinter import *


def keyGet(): #gets a random letter, a-z

    keysList = list(range(97,123)) #97-122 = a-z in ASCII
    #print(keysList) #//used for debugging

    global key
    key = str(chr(random.choice(keysList)))
    # ^^ converts a random number from 97-122 into a letter

    
def again():
    
    #pretty self-explanitory.

    #because this uses a while loop, it makes sure they can only type
    #"yes" or "no" by only moving forawrd once they type on of them.
    
    print("\n\nThanks for playing!\nWould you like to play again?")
    choice = ""
    
    while choice != "yes" and choice != "no":
        
        choice = input("\nType Either \"yes\" or \"no\": ")

        if choice == "yes":
            again = True
        elif choice == "no":
            again = False

    print("\n"*3)
    return again

gameLoop = True #as long as gameLoop is true, the game will run
while(gameLoop):

    global timer
    timer = 30 #How many seconds they have
    global mistakes
    mistakes = 5 #This is how many mistakes they can make

    turn = 0 #How many they've gotten right so far
    strikes = 0 #How many they've gotten wrong so far

    print("I'm gonna have you enter keys as they pop up on screen.")
    print("Are you ready for this?")
    print("You'll have %s seconds to hit as many keys as possible."%(timer))
    print("Each key you get correct will add 0.5 seconds to your time.")
    print("You can make %s mistakes.\n"%(mistakes))
    print("\nGet Ready!")
    time.sleep(7.5)
    
    ### ---- ###
    startTime = time.time()
    startTime = int(round(startTime))
    
    #--- these get and round 2 times (starting as the same time) to
    #--- be used as timers. by finding the difference between them,
    #--- you can count to 30 seconds as one rises and the other stays
    #--- the same.
    
    endTime = time.time()
    endTime = int(round(endTime))
    ### ---- ###

    while abs(endTime - startTime) < timer and strikes < mistakes:
        #this one loop makes sure they stay under the time limit and don't make too many mistakes

        keyGet()
        
        print("\nQuickly! Enter::   %s   "%(key))
        keyIN = str(input("\n::   "))

        if keyIN == key:
            print("Good Job!\n")
            turn += 1    #they made one more correct 'guess'
            timer += 0.5 #so they get some extra time
        elif keyIN != key:
            print("Oups!\n") 
            strikes += 1 #strike! 
            print("%s mistakes made."%(strikes))

        print("\n%s seconds left!"%(timer - abs(endTime-startTime)))
        
        endTime = time.time()
        endTime = int(round(endTime))
        
## -------------------------------------------
    ## end of while loop // at this point they will have either
    ## run out of time or hit the maximum allowed number of mistakes.
    ## so: we check which one it is:
## -------------------------------------------

    global timeTaken #declaring this before either of the if clauses use it
                     #mostly so python doesn't yell at me
        
    if abs(endTime - startTime) >= timer:
        
        endendTime = time.time()
        endendTime = int(round(endendTime))

        timeTaken = abs(endendTime - startTime)

            ## This 'endendTime' variable is a little weird.
            ## I use it because I already have 'endTime' as
            ## the variable that holds when a letter was entered.
            ## this way, I can find out when the game as a whole
            ## finished.
        
        print("\n\n\nOut of time!")
        print("You managed to enter %s keys correctly, and you made %s mistakes."%(turn, strikes))
        print("You stayed going for a total of %s seconds."%(timeTaken))
        
    elif strikes >= mistakes:
        
        endendTime = time.time()
        endendTime = int(round(endendTime))

        timeTaken = abs(endendTime - startTime)

            ## I guess I could have just redefined 'endTime', since it won't be used past this point
            ## but I preferred to have a different variable.
        
        print("\n\n\nYou've made too many mistakes! :O")
        print("You managed to enter %s keys correctly before hitting %s mistakes."%(turn, mistakes))
        print("You stayed going for a total of %s seconds."%(timeTaken))


    time.sleep(1.75)
 
    score = (turn * (round(timeTaken*1.75))) - (mistakes * 12)
 ## just a way I thought of to give a score that will give a representation of their abilities.
    print("\n\nYour final score is: %s points"%(score))
    
    gameLoop = again()

######-----------------------------------------######
######  I tried to use msvcrt.getch() to get   ######
######  keypresses without the need to hit     ######
######  the enter key, but I couldn't get it   ######
######  to work. I'll attach that test file    ######
######  to Google Classroom as well.           ######
######-----------------------------------------######
