from pokemon_maker import make_move, make_pokemon
from elements import elementer, check_effectiveness
from inputs import ask_for_pokemon
import random

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

move = make_move("waterfall")
pokemon = make_pokemon(ask_for_pokemon("pokemon here: "))

print(pokemon.elements)
print(check_effectiveness(pokemon, 0,  move))
print(check_effectiveness(pokemon, 1, move))

print(move.dmg_category)
