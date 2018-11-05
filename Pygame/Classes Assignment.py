class Animal():
    def __init__(self, nameInput):
        self.name = str(nameInput)
        print("An animal named", self.name, "has been born.")

    def eat(self, amount):

        amount = str(amount)
        
        if amount.isnumeric() == True:
            print(self.name, "eats " + amount + " foods.")
        else:
            print(self.name, "eats it's foods.")

    def make_noise(self):
        print(self.name, "says *rawr*")

class Cat(Animal):
    def __init__(self, nameInput):
        super().__init__(nameInput)
        print("The animal was a cat.\n")
        
    def make_noise(self):
        print(self.name,"says *nyaa*")

class Dog(Animal):
    def __init__(self, nameInput):
        super().__init__(nameInput)
        print("The animal was a dog.\n")
        
    def make_noise(self):
        print(self.name,"says *broof*")

##-----
        
cat = Cat("Coco")

dog1 = Dog("ChiChi")
dog2 = Dog("Mitzy")

lizz = Animal("Spike")

print("\n")

cat.eat(10)
dog1.eat(12)
dog2.eat(26)
lizz.eat('All')

print("\n")

cat.make_noise()
dog1.make_noise()
dog2.make_noise()
lizz.make_noise()
