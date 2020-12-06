from animal import Animal
from random import randint

class Mammal(Animal):
   
    gives_milk = True
    has_fur = True

    def __init__(self, animal_name, sound="Generic Mammal Noise"):
        super().__init__(animal_name, sound)
        

    def give_birth(self):
        babies = randint(1, 2)
        print(f"{self.name} has given birth to {babies} live animals because its a Mammal")

    def quiz(self):
        super().quiz()
        next_quiz = input("Do you want to take a quiz about mammals? [Y] [N] ")
        if next_quiz == "N":
            print("See you next time!")
        else:
            first_q = bool(input("Mammals tend to have fur. [True] [False] "))
            if first_q == Mammal.has_fur:
                print("Correct! Lets move on to the next question.")
                second_q = bool(input("Mammals are known for giving milk to their offsprings. [True] [False] "))
                if second_q == Mammal.gives_milk:
                    print("Congrats! You nailed the quiz!")
                else:
                    print("Sorry! You only awnsered 1/2 questions right. See you next time!")
            else:
                print("Sorry! You didn't get any questions right. See you next time!")

