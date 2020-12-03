from mammal import Mammal
from random import randint
from oviparous import Oviparous

class Platypus(Mammal, Oviparous):
    
    def __init__(self, animal_name, sound="Perry the platypus!"):
        super().__init__(animal_name, sound)
        
    ''' This method is a mix in from the Oviparous class'''
    def give_birth(self):
       Oviparous.give_birth(self)


