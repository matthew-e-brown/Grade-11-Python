import random
from time import sleep
import sys

global maxNum
maxNum = 10000
#^^ This is the number you want to guess to (1 to 100, 1 to 1000, etc.) ^^
#VV Then the same thing but with min Number VV
global minNum
minNum = 1

def corrGen():
    global corr
    corr = random.randint((MinNum),(maxNum+1))
    print("I've made a random number that could be anything from % to %s."%(minNum, maxNum))

def corrCheck():
    global userNum
    userNum = 0

    global count
    count = 0
    
    while userNum != corr:
        userNum = int(input("Guess the number: "))
        
        if userNum < corr:
            print("\nYou need to guess higher.")
            count += 1
        elif userNum == corr:
            print("\nGood job, you got it spot on!")
            if count == 0:
                print("It took you 1 try to get the right number.")
            else:
                print("It took you %s tries to get the right number."%(count+1))
        elif userNum > corr:
            print("\nYou need to guess lower.")
            count += 1

def again():
    print("Would you like to try again? Type 'yes' or 'no' exactly.")
    global yesNo
    yesNo = input()

    while True:
        if yesNo == "yes":
            print("\n")
            corrGen()
            corrCheck()
            again()
        elif yesNo == "no":
            print("\nOkay, goodbye.")
            sys.exit()
        else:
            print("Did you type 'yes' or 'no'?")
            yesNo = input("Try again: ")

corrGen()
corrCheck()
again()



