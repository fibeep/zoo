from random import randint
from animal import Animal


class Oviparous(Animal):
    
    lay_egg = True

    def __init__(self, animal_name, sound="Oviparous sounds"):
        super().__init__(animal_name, sound)
        
    
    def give_birth(self):
        babies = randint(1, 5)
        print(f"{self.name} has layed, {babies} eggs")
