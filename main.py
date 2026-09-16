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


from move_class import Move
from pokemon_class import Pokemon
from move_bank import *
from battle import pokemon_battle, calculate_dmg
    

charizard = Pokemon("charizard", "fire", 100, 90, 70, 70, 50, 65, [flamethrower, scratch, gun])
bulbasaur = Pokemon("bulbasaur", "grass", 45, 49, 49, 65, 65, 45, [Seed_Bomb, grass_knot, scratch])
venusaur = Pokemon("venusaur", "grass", 80, 82, 83, 100, 100, 80, [Solar_Beam, Razor_Leaf])
testmon = Pokemon("testmon", "test_element", 1,1,1,1,1,1)

# charizard.take_damage(50)

# charizard.take_damage(20)
# charizard.take_damage(10)
# charizard.take_damage(0.5)
# charizard.take_damage(0.05)

# charizard.talk()
# bulbasaur.talk()
# testmon.talk()


your_pokemon = charizard
enemy_pokemon = venusaur
        
    
# pokemon_battle(your_pokemon, enemy_pokemon)

trainer = [venusaur, bulbasaur]

print(f"du er i en kamp mot trainer, de har {len(trainer)} pokemon")

for trainers_pokemon in trainer:
    pokemon_battle(your_pokemon, trainers_pokemon)
    print(f"det er {len(trainer)-1} pokemon igjen")