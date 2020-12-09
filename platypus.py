from mammal import Mammal
from random import randint
from oviparous import Oviparous

class Platypus(Mammal, Oviparous):

    natures_mix_and_match = True
    __perry_the_platypus = True
    
    def __init__(self, animal_name, sound="Perry the platypus!"):
        super().__init__(animal_name, sound)
        
    ''' This method is an override in from the mammal and oviparous class'''
    
    def give_birth(self):
       babies = randint(1, 5)
       print(f"{self.name} has layed {babies} eggs although it is a mammal.")

    def quiz(self):
        Mammal.quiz(self)
        Oviparous.quiz(self)
        platypus_game = input("Do you want to awnser questions about platipuses? [Y] [N] ")
        if platypus_game == "Y":
            response = bool(input('Is the most famous platypus of all time named perry? Respond True or hit enter for False: '))
            if response == Platypus.__perry_the_platypus:
                print("Good job!")
            else:
                print("Please go watch phineas and pherb")
            pass
        else:
            print("Okay, see you next time!")
        
    
