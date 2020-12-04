from random import randint
from animal import Animal


class Oviparous(Animal):
    
    lay_egg = True
    warm_blooded = False

    def __init__(self, animal_name, sound="Oviparous sounds"):
        super().__init__(animal_name, sound)
        
    
    def give_birth(self):
        babies = randint(1, 12)
        print(f"{self.name} has layed, {babies} eggs")
