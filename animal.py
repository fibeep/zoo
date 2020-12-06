from random import randint


class Animal:
    
    eats_food = True
    drinks_water = True
    reproduces = True

    def __init__(self, animal_name, sound="Generic Animal Noise"):
        self.name = animal_name
        self.sound = sound
        # The website ID is an ID that can be used to localize our animals in the zoo website
        self._website_id = randint(10000,99999)
        # The internal ID is keep track of the animals internally
        self.__internal_id = randint(100000, 999999)


    def give_birth(self):
        babies = randint(1,5)
        print(f"{self.name} has spawned {babies} offsprings")
    
    def speak(self):
        print(self.sound, self.sound)

    def quiz(self):
        answer1 = bool(input("Do animals eat food? Respond True or hit enter for False: "))
        if answer1 == Animal.eats_food:
            print("Correct!")
            answer2 = bool(input("Do animals drink water? Respond True or hit enter for False: "))
            if answer2 == Animal.drinks_water:
                print("Correct!")
                answer3 = bool(input("Do animals reproduce? Respond True or hit enter for False: "))
                if answer3 == Animal.reproduces:
                    print("Correct! You have awnsered all questions right!")
                else:
                    print("Sorry! You only awnsered 2/3 questions right")
            else:
                print("Incorrect, only 1/3 awnsers right!")
        else:
            print("Sorry! You have awnsered wrong")
        

