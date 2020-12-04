from mammal import Mammal
from random import randint
from oviparous import Oviparous

class Platypus(Mammal, Oviparous):
    
    def __init__(self, animal_name, sound="Perry the platypus!"):
        super().__init__(animal_name, sound)
        
    ''' This method is an override in from the mammal and oviparous class'''
    
    def give_birth(self):
       babies = randint(1, 5)
       print(f"{self.name} has layed {babies} eggs although it is a mammal.")

    def quiz(self):
        super().quiz()
        # Mammal.quiz(self)
        # Oviparous.quiz(self) -> Check multiple inheritance slides
        platypus_game = input("Do you want to awnser questions about platipuses? [Y] [N] ")
        if platypus_game == "Y":
            # Make platypus quiz
            pass
        else:
            print("Okay, see you next time!")
