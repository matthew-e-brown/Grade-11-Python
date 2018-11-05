import random
from time import sleep
from time import time

global count
count = 1

UserNums = []

def getNums():
    for i in range(0,6):
        luckIN = input("Input your lucky number for %s spot: "%(i+1))
        
        if luckIN.isnumeric() == True:
            while int(luckIN) >= 50 or int(luckIN) < 1:
                print("Please only use numbers below or equal to 49. And not zero.")
                luckIN = input("Input your lucky number for %s spot: "%(i+1))
    
            if int(luckIN) not in UserNums:
                UserNums.append(int(luckIN))
                    
            elif int(luckIN) in UserNums:
                print("Use each number only once.")
                
                while int(luckIN) in UserNums:
                    luckIN = input("Input your lucky number for %s spot: "%(i+1))
                UserNums.append(int(luckIN))
                
                
        elif luckIN.isnumeric() == False:
            print("Use only numbers. Try again.")
            luckIN = input("Input your lucky number for %s spot: "%(i+1))
            
    UserNums.sort()
            
#Gets UserNums
getNums()
print("\nYour list is:")
print(UserNums)

sleep(1)

#Gets LuckyNums
Nums = list(range(1,50))
random.shuffle(Nums)
LuckyNums = Nums[0:6]
LuckyNums.sort()

#Prints LuckyNums
print ("\nThe Drawn numbers are:")
sleep(1)
print(LuckyNums)
print("\n")

#Find Matches
Matches = set(UserNums) & set(LuckyNums)

if len(Matches) != 6:

    #Print what matched
    print("\nYou matched %s numbers."%(len(Matches)))
    sleep(1)
    print("\nYou matched: %s"%(Matches))
    print("\n")
    
    sleep(2)
    
    print("That didn't work out for you. How about I enter you into an\ninfinite number of draws until you win?")

    sleep(5)

    startTime = time()

    print("\nRunning...")
    
    while len(Matches) != 6:
        Nums = list(range(1,50))
        random.shuffle(Nums)
        LuckyNums = Nums[0:6]
        LuckyNums.sort()
        #print(LuckyNums)
        count = count + 1
        
        if count % 1000000 == 0:
            millTime = time()
            elapsed = millTime - startTime
            elapsed = int(elapsed*100+0.5)/100
            print("\nIt took %s seconds to reach %s draws." %(elapsed, count))
        
else:

    print("\nYou Won!!")
    sleep(1)
    print("Details:")
    
    Matches = set(UserNums) & set(LuckyNums)

    print("\nYou matched: %s"%(Matches))
    sleep(1)
    print("\nYou matched %s numbers."%(len(Matches)))
    sleep(1)
    
    if count > 1:
        print("\nIt took you %s draws to win with your number combination."%(count))
    elif count == 1:
        print("\nIt took you %s draw to win with your number combination."%(count))
