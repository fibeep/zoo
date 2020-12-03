from animal import Animal
from platypus import Platypus
from mammal import Mammal
from oviparous import Oviparous
from zoo import Zoo

salosZoo = Zoo("My Zoo", "San Francisco", 30)
Hippo = Animal("Hippopotamus")
salosZoo.create_animal(Hippo)

salosZoo.show_animals()

print(salosZoo.animals_left)
