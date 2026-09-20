from move_class import Move
from pokemon_class import Pokemon
from move_bank import *
from battle import pokemon_battle, calculate_dmg
from pokemon_maker import make_pokemon, does_pokemon_exist
from inputs import ask_for_pokemon

charizard = Pokemon("charizard", "fire", "None",100, 90, 70, 70, 50, 65, [flamethrower, scratch, gun])
bulbasaur = Pokemon("bulbasaur", "grass", "None", 45, 49, 49, 65, 65, 45, [Seed_Bomb, grass_knot, scratch])
venusaur = Pokemon("venusaur", "grass", "poison", 80, 82, 83, 100, 100, 80, [Solar_Beam, Razor_Leaf])
testmon = Pokemon("testmon", "test_element", "None", 1,1,1,1,1,1)


# your_pokemon = charizard
# enemy_pokemon = venusaur
    
# pokemon_battle(your_pokemon, enemy_pokemon)

# trainer = [venusaur, bulbasaur, testmon]

# print(f"du er i en kamp mot trainer, de har {len(trainer)} pokemon")

# for trainers_pokemon in trainer:
#     pokemon_battle(your_pokemon, trainers_pokemon)

# lopunny = make_pokemon("lopunny")
# print(lopunny.name, lopunny.moves[0].name, lopunny.moves[1].name, lopunny.moves[2].name, lopunny.moves[3].name)

testing = make_pokemon("charizard", ["flamethrower", "focus-punch"])

print(testing.moves[1].power)

your_pokemon_name = ask_for_pokemon("Hvilken pokmeon vil du ha?: ")
enemy_pokemon_name = ask_for_pokemon("Hvilken pokemon vil du slåss mot?: ")

your_pokemon = make_pokemon(your_pokemon_name)
enemy_pokemon = make_pokemon(enemy_pokemon_name)


pokemon_battle(your_pokemon, enemy_pokemon)