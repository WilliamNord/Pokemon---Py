import random
from pokemon_maker import *
from pokemon_class import *
from player_class import *
from pokeball_class import *
from elements import *
from inputs import *
from battle import *

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

# for i in range(0):
#     print(i)

# print()
# for x, y in enumerate(["jeg", "deg"]):
#     print(type(x), x)
#     print(type(y), y)

# print()
# for x in enumerate(["jeg", "deg"]):
#     print(type(x), x)

# print()
# for x, (y,z) in enumerate([["jeg", "deg"], ["du", "meg"]]):
#     print(type(x), x)
#     print(type(y), y)
#     print(type(z), z)

# print()
# for x, indre_liste in enumerate([["jeg", "deg"], ["du", "meg"]]):
#     for y, z in enumerate(indre_liste):
#         print(x, y, z)
    
# while True:
#     your = make_pokemon("machamp")
#     enemy = make_pokemon("seedot")
#     pokemon_battle(your, enemy)
    
# hit = 0
# tot = 0
# for i in range(1000000):
#     if is_critical() == 1:
#         hit += 1
#         tot += 1
#     else:
#         tot += 1
# print(f"chance: {(hit/tot)*100}")


# move = make_move("focus-blast")
# print(move.accuracy)

# hit = 0
# for i in range(100):
#     if check_for_accuracy(move):
#         hit += 1

# print(f"chance: {hit/ 100}")

# pkm = make_pokemon("iron-hands")
# print(pkm.moves)
# print(len(pkm.moves))
# print("random move:", pick_random_move(pkm))

# liste = ["home", "school"]
# print(liste.index("home"))

# if type(liste.index("hime")) == int:
#     print("it is int")
# print(make_pokemon(level=5, pokemon_name="charmander").level)
# print(ask_player_location(liste), type(ask_player_location(liste)))

# pokemon = ask_for_pokemon("pokemon: ")
# data_test = get_api_data(f"pokemon/{pokemon}")
# print(get_moves_available_for_lvl(data_test, 100)[0])
# print(get_moves_available_for_lvl(data_test, 100)[0][-4:])

# pkm: Pokemon = make_pokemon("charmander", ["fire-punch"], 100)
# pkm2: Pokemon = make_pokemon("charmander", None, 100)

# for name in pkm.moves:
#     print(name.name)

# print("pkm2:")
# for name in pkm2.moves:
#     print(name.name)

# thing = []
# if not thing:
#     print("ye")

# flot = 1.5
# print(int(flot))

# dicto = {
#     "amount": 0
# }

# for i in range(10):
#     dicto["amount"] += 1

# print(dicto)
# print((lambda n: n**3)(2)) # 8
p = Player("johan")
print()

p.add_pokeballs("pokeball", 10)
p.add_pokeballs("greatball", 2)
p.add_pokeballs("ultraball", 1)

print(p.get_available_pkbls())