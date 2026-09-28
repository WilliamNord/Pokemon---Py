from pokemon_maker import make_move, make_pokemon
from pokemon_class import Pokemon
from elements import all_elements, check_effectiveness
from inputs import ask_for_pokemon
import random
from battle import pokemon_battle, is_critical

# print(charizard.calculate_stat("attack"))
# print(charizard.calculate_stat("hp"))

# your_pokemon = charizard
# enemy_pokemon = venusaur
    
# pokemon_battle(your_pokemon, enemy_pokemon)

# trainer = [venusaur, bulbasaur, testmon]

# print(f"du er i en kamp mot trainer, de har {len(trainer)} pokemon")

# for trainers_pokemon in trainer:
#     pokemon_battle(your_pokemon, trainers_pokemon)

# lopunny = make_pokemon("lopunny")
# print(lopunny.name, lopunny.moves[0].name, lopunny.moves[1].name, lopunny.moves[2].name, lopunny.moves[3].name)

# testing = make_pokemon("charizard", ["flamethrower", "focus-punch"])

# print(testing.moves[1].power)

# random.randint(85, 100)

# tall = 0
# for i in range(100):
#     tall = random.randint(85, 100) / 100
#     print(tall)

# move = make_move("waterfall")
# pokemon = make_pokemon(ask_for_pokemon("pokemon here: "))

# print(pokemon.elements)
# print(check_effectiveness(pokemon, 0,  move))
# print(check_effectiveness(pokemon, 1, move))

# print(move.dmg_category)

for i in range(0):
    print(i)

print()
for x, y in enumerate(["jeg", "deg"]):
    print(type(x), x)
    print(type(y), y)

print()
for x in enumerate(["jeg", "deg"]):
    print(type(x), x)

print()
for x, (y,z) in enumerate([["jeg", "deg"], ["du", "meg"]]):
    print(type(x), x)
    print(type(y), y)
    print(type(z), z)

print()
for x, indre_liste in enumerate([["jeg", "deg"], ["du", "meg"]]):
    for y, z in enumerate(indre_liste):
        print(x, y, z)
    
# while True:
#     bulb = make_pokemon("bulbasaur",["vine-whip"], 5)
#     char = make_pokemon("charmander", ["fire-punch"], 5)
#     pokemon_battle(char, bulb)
    
# hit = 0
# tot = 0
# for i in range(1000000):
#     if is_critical() == 1:
#         hit += 1
#         tot += 1
#     else:
#         tot += 1
# print(f"chance: {(hit/tot)*100}")