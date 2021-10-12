import random

# TODO: Define the Thrower class here.
class Thrower():

    def __init__(self):
        self.myDice = [1,2,3,4,5,6]
        self.dice = random.choices(self.myDice, k=5)
        self.points = 0
        self.can_Throw = True

    def can_throw(self):
        if 5 or 1 in self.dice:
            print("True")
            return True
        else: 
            print("False!")
            return False
            
        

            
    def get_points(self):
        print(self.dice)
        #if self.thrown_dice == 5:
        if 5 in self.dice:
            print(self.dice)
            self.points += 50

        if 1 in self.dice:
            self.points += 100

        print(f'Points: {self.points}')
        return self.points

    def throw_dice(self):
        
       # while True:
            self.dice = random.choices(self.dice, k=5)
            return self.dice
                

# relace thrown dice to dice
