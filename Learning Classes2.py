import random

class Boat():
    def __init__(self, new_tonnage, new_name):
        self.tonnage = new_tonnage
        self.name = new_name
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print(self.name, "is already docked, dummy")
        else:
            self.is_docked = True
            print(self.name, "is docking")

    def undock(self):
        if not self.is_docked:
            print(self.name, "is not docked.")
        else:
            self.is_docked = False
            print(self.name, "is undocking")

bb = Boat(30, "JayJay")

class Submarine(Boat):    
    def submerge(self):
        print(self.name, "is going under, glug glug")

ss = Submarine(5, "Red December")
ss.dock()
ss.undock()
ss.submerge()

bb.undock()




