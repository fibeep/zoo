from animal import Animal
from platypus import Platypus
from mammal import Mammal
from oviparous import Oviparous




class Zoo:
    
    holds_animals = True

    def __init__(self, name, location, max_animals):
        self.name = name
        self.location = location
        self.max_animals = max_animals
        self.animals_left = max_animals
        self.current_animals = []

    def create_animal(self):
        ''' This function creates an animal by passing in the animal and the amount'''
        amount = int(input("How many animals would you like to make? "))
        if self.animals_left < amount:
            print("There is no more space available in your zoo, please expand it or sell an animal.")
        else:
            animal = input("What type of animal are you creating? ")
            animal_name = input("Please name your animal ")
            species = eval(input("What species is your animal? (Animal) (Mammal) (Platypus) (Oviparous) "))
            sound = input("What sound does your animal make? ")
            animal = species(animal_name, sound)
            self.animals_left -= amount
            for _ in range(0, amount):
                self.current_animals.append(animal)
            print(f"You now have {self.animals_left} spots available")
    
    def expand_zoo(self, expansion):
        self.max_animals += expansion
        self.animals_left += expansion
        print(f"You have sucessfully expanded your zoo. The maximum amount of animals you can host is now {self.max_animals} which means you can now have {self.animals_left} more animals.")

    def show_animals(self):
        for animal in self.current_animals:
            print(animal)


salosZoo = Zoo("My Zoo", "San Francisco", 30)

salosZoo.create_animal()

for animal in salosZoo.current_animals:
    print(animal.name)

