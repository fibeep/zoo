from animal import Animal
from platypus import Platypus
from mammal import Mammal
from oviparous import Oviparous


class Zoo:
    
    def __init__(self, name, location, max_animals):
        self.name = name
        self.location = location
        self.max_animals = max_animals
        self.animals_left = max_animals
        self.current_animals = []

    def create_animal(self, animal, amount=1):
        ''' This function creates an animal by passing in the animal and the amount'''
        
        if self.animals_left < amount:
            print("There is no more space available in your zoo, please expand it or sell an animal.")
        else:
            self.animals_left -= amount
            for _ in range(0, amount):
                self.current_animals.append(animal)
    
    def expand_zoo(self, expansion):
        self.max_animals += expansion
        self.animals_left += expansion
        print(f"You have sucessfully expanded your zoo. The maximum amount of animals you can host is now {self.max_animals} which means you can now have {self.animals_left} more animals.")

    def show_animals(self):
        for animal in self.current_animals:
            print(animal.name)




salosZoo = Zoo("My Zoo", "San Francisco", 30)
Hippo = Animal("Hippopotamus")
salosZoo.create_animal(Hippo)

salosZoo.show_animals()

