from animal import Animal
from random import randint

class Mammal(Animal):
   
    def __init__(self, animal_name, sound="Generic Mammal Noise"):
        super().__init__(animal_name, sound)
        self.gives_milk = True

    def give_birth(self):
        babies = randint(1, 5)
        print(f"{self.name} has given birth to {babies} live animals because its a Mammal")

