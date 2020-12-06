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

    def quiz(self):
        super().quiz()
        next_quiz = input("Do you want to take a quiz about Oviparous Animals? [Y] [N] ")
        if next_quiz == "N":
            print("See you next time!")
        else:
            first_q = bool(input("Oviparous tend to be warm blooded. [True] [False] "))
            if first_q == Oviparous.warm_blooded:
                print("Correct! Lets move on to the next question.")
                second_q = bool(
                    input("Oviparous animals lay eggs. [True] [False] "))
                if second_q == Oviparous.lay_egg:
                    print("Congrats! You nailed the quiz!")
                else:
                    print(
                        "Sorry! You only awnsered 1/2 questions right. See you next time!")
            else:
                print("Sorry! You didn't get any questions right. See you next time!")
