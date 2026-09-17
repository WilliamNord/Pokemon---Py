from move_class import Move
from pokemon_class import Pokemon
from move_bank import *
from battle import pokemon_battle, calculate_dmg
    

charizard = Pokemon("charizard", "fire", 100, 90, 70, 70, 50, 65, [flamethrower, scratch, gun])
bulbasaur = Pokemon("bulbasaur", "grass", 45, 49, 49, 65, 65, 45, [Seed_Bomb, grass_knot, scratch])
venusaur = Pokemon("venusaur", "grass", 80, 82, 83, 100, 100, 80, [Solar_Beam, Razor_Leaf])
testmon = Pokemon("testmon", "test_element", 1,1,1,1,1,1)


your_pokemon = charizard
enemy_pokemon = venusaur
    
# pokemon_battle(your_pokemon, enemy_pokemon)

trainer = [venusaur, bulbasaur, charizard]

print(f"du er i en kamp mot trainer, de har {len(trainer)} pokemon")

for trainers_pokemon in trainer:
    pokemon_battle(your_pokemon, trainers_pokemon)