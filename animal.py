from random import randint


class Animal:
    
    eats_food = True
    drinks_water = True
    reproduces = True

    def __init__(self, animal_name, sound="Generic Animal Noise"):
        self.name = animal_name
        self.sound = sound

    def give_birth(self):
        babies = randint(1,5)
        print(f"{self.name} has spawned {babies} offsprings")
