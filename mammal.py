from animal import Animal
from random import randint

class Mammal(Animal):
   
    gives_milk = True
    has_fur = True

    def __init__(self, animal_name, sound="Generic Mammal Noise"):
        super().__init__(animal_name, sound)
        

    def give_birth(self):
        babies = randint(1, 2)
        print(f"{self.name} has given birth to {babies} live animals because its a Mammal")

