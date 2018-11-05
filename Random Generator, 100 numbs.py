import random

random.seed(10)

print ("Numbers between 1 and 100")

nums = []

for i in range (0,100):
    a = random.randint(1,100)
    nums.append(a)

nums.sort()
print(nums)
