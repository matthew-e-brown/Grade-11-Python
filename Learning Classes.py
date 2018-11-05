import random

''' Define the class Cat '''
class Cat:
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print(self.name,"says MEOW")

    def joy(self):
        print(self.name,"is just happy to be there.")

''' Create an instance of 'Cat' '''
chanel = Cat()
chanel.name = "Chanel"
chanel.color = "Amber"
chanel.weight = 3.2

chanel.meow()
print("\n")
chanel.joy()

coco = Cat()
coco.name = "Coco"
coco.color = "White and Brown"
coco.weight = 4.6

coco.meow()
print("\n")
coco.joy()

class Monster:
    def __init__(self):
        self.name = ""
        self.health = 0

    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(self.name,"has died!")
        else:
            print(self.name,"has",self.health,"health pointerinos left.")

jerk = Monster()
jerk.name = "Evil Bastard"
jerk.health = random.randint(1,10000)

ass = Monster()
ass.name = "Cooniggulosaurus Rex"
ass.health = random.randint(1,100000)

print("\n")

while jerk.health > 0:
    attack_strength = int(input("How hard are you gonna hit %s? ::: "%(jerk.name)))
    jerk.decrease_health(attack_strength)
    if jerk.health > 0:
        print("He's still alive! Hit him again!\n")

print(jerk.name,"is dead! Hooray!")

print("\n"*2)
print("Another one!")

while ass.health > 0:
    attack_strength = int(input("How hard are you gonna hit %s? ::: "%(ass.name)))
    ass.decrease_health(attack_strength)
    if ass.health > 0:
        print("It's still alive! Hit him again!\n")

print(ass.name,"is dead! Hooray!")
