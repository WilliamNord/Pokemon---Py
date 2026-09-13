# class Person:
#     def __init__(self, name: str, age:int , fav_color: str):
#         self.name = name
#         self.fav_color = fav_color
#         self.age = age
    
#     def hilsen(self):
#         print(f"jeg hater {self.name}, jeg er {self.age} år gammer og jeg liker fargen {self.fav_color}")
        
# john = Person("john", 48, "Blue")
# hilde = Person("hilde", 26, "Grønn")
# john.hilsen()
# hilde.hilsen()

#metode for super effektive typer
elementer = {
    "fire": {
        "strong": ["ice", "grass", "metal", "bug"],
        "weak": ["ground", "water", "rock",],
        },
    "water": {
        "strong": ["fire", "ground","electric"],
        "weak": ["grass", "electric"],
    }
}

print(elementer["fire"]["strong"][0])

from move_class import Move
from pokemon_class import Pokemon
from move_bank import *
from battle import *
    

charizard = Pokemon("charizard", "fire", 100, 70, 90, 70, 50, 65, [flamethrower, scratch, gun])
bulbasaur = Pokemon("bulbasaur", "grass", 45, 49, 49, 65, 65, 45, [grass_knot, scratch])
testmon = Pokemon("testmon", "test_element", 1,1,1,1,1,1)

# charizard.take_damage(50)

# charizard.take_damage(20)
# charizard.take_damage(10)
# charizard.take_damage(0.5)
# charizard.take_damage(0.05)


charizard.talk()
bulbasaur.talk()
testmon.talk()


your_pokemon = charizard
enemy_pokemon = bulbasaur
        
    
battle(your_pokemon, enemy_pokemon)
