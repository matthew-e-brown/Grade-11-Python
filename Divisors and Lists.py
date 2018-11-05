print("Input a number.")

num = input("Preferrably not too high: ")

while num.isnumeric() != True:
    num = input("Please use a number: ")

divs=[]

for x in range(1,int(num)+1):
    if int(num) % x == 0:
        divs.append(int(x))

print("The divisors of that number are: %s." %(divs))

