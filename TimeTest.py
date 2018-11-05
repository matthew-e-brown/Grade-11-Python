import time

startTime = time.time()

count = 1

while (count<1000):
    count += 1
    print(count)
    
endTime = time.time()

print("It took %s seconds to count to %s." %(endTime - startTime, count))
