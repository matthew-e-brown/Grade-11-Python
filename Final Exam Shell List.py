Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(1, 49): print(i)
print(i)
SyntaxError: invalid syntax
>>> for i in range(1, 49):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
>>> nums = []
>>> for i in range(1, 50):
	nums.append(i)

	
>>> nums.shuffle()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    nums.shuffle()
AttributeError: 'list' object has no attribute 'shuffle'
>>> print(nums)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> import random
>>> random.shuffle(nums)
>>> print(nums)
[32, 3, 40, 16, 6, 31, 49, 9, 4, 22, 7, 43, 12, 37, 24, 2, 47, 5, 41, 19, 33, 21, 28, 26, 23, 36, 30, 13, 29, 1, 35, 11, 34, 25, 18, 48, 38, 15, 8, 46, 20, 44, 10, 17, 27, 45, 42, 14, 39]
>>> lucknums = nums[:6]
>>> print(lucknums)
[32, 3, 40, 16, 6, 31]
>>> lucknums.sort()
>>> print(lucknums)
[3, 6, 16, 31, 32, 40]
>>> def check():
	if num > 0 and num != 3:
		print("True")

		
>>> num = 65
>>> check()
True
>>> num = 2
>>> check()
True
>>> num = 3
>>> check()
>>> def check():
	if num > 0 and num != 3:
		print("True")
	else:
		print("False")

		
>>> num = 3
>>> check()
False
>>> 
=============================== RESTART: Shell ===============================
>>> print(num)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(num)
NameError: name 'num' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> iceCream = True
>>> candy = True
>>> peanuts = False
>>> if iceCream and not(peanuts):
	print("so sad")

	
so sad
>>> if iceCream or not(peanuts):
	print("too bad")

	
too bad
>>> if peanuts or iceCream and not(candy):
	print("ya!")

	
>>> 
=============================== RESTART: Shell ===============================
>>> def check():
	if num % 2 == 0:
		print("even")
	elif: num.isnumeric() == False:
		
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> def check():
	if num % 2 == 0:
		print("even")
	elif num.isnumeric() == False:
		print("type a number")
	else:
		print("odd")

		
>>> num = 3
>>> check()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    check()
  File "<pyshell#59>", line 4, in check
    elif num.isnumeric() == False:
AttributeError: 'int' object has no attribute 'isnumeric'
>>> def check():
	if num % 2 == 0:
		print("even")
	elif str(num).isnumeric() == False:
		print("type a number")
	else:
		print("odd")

		
>>> check()
odd
>>> num = 4
>>> check()
even
>>> num = "asd"
>>> check()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    check()
  File "<pyshell#63>", line 2, in check
    if num % 2 == 0:
TypeError: not all arguments converted during string formatting
>>> def check():
	if num % 2 == 0:
		print("even")
	elif str(num).isnumeric() == False:
		print("type a number")
	else:
		print("odd")

		
>>> 
=============================== RESTART: Shell ===============================
>>> import random
>>> print(list(random.randrange(0, 99)))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(list(random.randrange(0, 99)))
TypeError: 'int' object is not iterable
>>> l = random.randrange(0, 99)
>>> print(l)
70
>>> l = []
>>> for i in range(0, 99)
SyntaxError: invalid syntax
>>> for i in range(0, 99):
	i = random.randint(0, 99)
	l.append(i)

	
>>> if 99 in l:
	print("bingo")

	
bingo
>>> print(l)
[41, 67, 64, 0, 90, 16, 41, 39, 83, 66, 84, 26, 12, 32, 31, 85, 97, 82, 75, 73, 69, 69, 49, 86, 35, 96, 6, 4, 51, 95, 11, 41, 56, 47, 19, 4, 77, 22, 94, 74, 30, 82, 34, 77, 15, 3, 32, 49, 67, 97, 94, 97, 30, 69, 32, 75, 64, 27, 29, 79, 72, 24, 75, 87, 69, 61, 65, 27, 81, 46, 30, 69, 48, 78, 36, 9, 40, 81, 15, 99, 4, 91, 53, 66, 55, 52, 7, 87, 50, 69, 41, 34, 7, 40, 57, 58, 85, 48, 23]
>>> l.sort()
>>> print(l)
[0, 3, 4, 4, 4, 6, 7, 7, 9, 11, 12, 15, 15, 16, 19, 22, 23, 24, 26, 27, 27, 29, 30, 30, 30, 31, 32, 32, 32, 34, 34, 35, 36, 39, 40, 40, 41, 41, 41, 41, 46, 47, 48, 48, 49, 49, 50, 51, 52, 53, 55, 56, 57, 58, 61, 64, 64, 65, 66, 66, 67, 67, 69, 69, 69, 69, 69, 69, 72, 73, 74, 75, 75, 75, 77, 77, 78, 79, 81, 81, 82, 82, 83, 84, 85, 85, 86, 87, 87, 90, 91, 94, 94, 95, 96, 97, 97, 97, 99]
>>> mark = input("Your mark is?? ::")
Your mark is?? ::95
>>> print(mark)
95
>>> 
=============================== RESTART: Shell ===============================
>>> def check():
	if mark.isnumeric() == True:
		mark = int(mark)

		
>>> def check():
	if mark.isnumeric() == True:
		mark = int(mark)
		if mark >= 50:
			print("You're passing!")
			if mark >= 80:
				print("You're in the honour roll, too!")
		elif mark < 50:
			print("... You should try harder next year... when you redo this one.")
	else: print("type a number.")

	
>>> mark = 23
>>> check()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    check()
  File "<pyshell#102>", line 2, in check
    if mark.isnumeric() == True:
UnboundLocalError: local variable 'mark' referenced before assignment
>>> global mark
>>> mark = 43
>>> check()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    check()
  File "<pyshell#102>", line 2, in check
    if mark.isnumeric() == True:
UnboundLocalError: local variable 'mark' referenced before assignment
>>> 
=============================== RESTART: Shell ===============================
>>> def pass():
	
SyntaxError: invalid syntax
>>> def check():
	if str(mark).isnumeric() == True:
		mark = int(mark)
		if mark >= 50:
			print("you're passing!")
			if mark >= 80:
				print("you're in honours")
		elif mark < 50:
			print("fail")
	else:
		print("type number")

		
>>> mark = "32"
>>> check()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    check()
  File "<pyshell#120>", line 2, in check
    if str(mark).isnumeric() == True:
UnboundLocalError: local variable 'mark' referenced before assignment
>>> 	if str(mark).isnumeric() == True:
		mark = int(mark)
		if mark >= 50:
			print("you're passing!")
			if mark >= 80:
				print("you're in honours")
		elif mark < 50:
			print("fail")
	else:
		print("type number")
		
SyntaxError: unexpected indent
>>> 
=============================== RESTART: Shell ===============================
>>> mark = 32
>>> if mark.isnumeric() == True: print("yes")

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    if mark.isnumeric() == True: print("yes")
AttributeError: 'int' object has no attribute 'isnumeric'
>>> if str(mark).isnumeric() == True: print('yes')

yes
>>> 
=============================== RESTART: Shell ===============================
>>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> lessthan = []
>>> for i in range(0, len(a)):
	if a[i] < 5:
		lessthan.append(a[i])

		
>>> print(lessthan)
[1, 1, 2, 3]
>>> 