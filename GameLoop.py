import random, time

# This function returns True if the user
# wishes to play again, and False otherwise.
def playAgain():
    print("Do you want to play again?")
    choice = ""
    while choice != "n" and choice != "y":
        
        print("(Press n to quit, type y to play again.)\n")
        
        choice = input()
        if choice == 'n':
            r = False
        elif choice == 'y':
            r = True

    return r

# game flag : True means keep playing
#           : False means stop the game

game = True
while (game):
    # Your game code goes here
    #

    print("Answer this math question:")
    time.sleep(1)
    a = random.randint(10,20)
    b = random.randint(10,20)
    
    print("What is %s x %s ?"%(a,b))
    num = int(input())
    time.sleep(0.5)
    if num == a*b:
        print("You are RIGHT :)")
    else:
        print("WRONG!!!")

    # Call the playAgain function
    # Update the game flag
    game = playAgain()

print("Thanks for playing!!")
