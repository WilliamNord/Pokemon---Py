from inputs import ask_player_choice
from player_class import Player
from pokemon_maker import make_pokemon
from battle import pokemon_battle
from render import clear_screen
from inputs import go_back_return
import math
import random

player = Player("John pokemon")
charizard = make_pokemon("charmander", level=5, move_names=["flamethrower"])
player.add_pokemon(charizard)

routes = {
    "route_1": {
        "route name": "Route 1",
        "possible_pokemon": [
            ("pidgey", 40),
            ("rattata", 30),
            ("oddish", 30),
            ("bellsprout", 30),
        ],
        "min_lvl": 2,
        "max_lvl": 4,
    },
    "route_100": {
        "route name": "Route_100",
        "possible_pokemon": [
            ("dragonite", 50),
            ("dratini", 10),
        ],
        "min_lvl": 50,
        "max_lvl": 100
    }
        
}

def make_wild_pokemon(route: dict):
    possible_pokemon = route["possible_pokemon"]
    min_lvl = route["min_lvl"]
    max_lvl = route["max_lvl"]
    chance_list = []
    for pokemon in possible_pokemon:
        weight_number = int(math.trunc(pokemon[1]))
        name = pokemon[0]
        for i in range (weight_number):
            chance_list.append(name)
    
    random_level = random.randint(min_lvl, max_lvl)
    random_index = random.randint(0, len(chance_list)-1)
    pokemon_name = chance_list[random_index]
    
    pokemon = make_pokemon(pokemon_name = pokemon_name, level = random_level)
    print(pokemon.name)
    return pokemon


route_options = list(routes.keys())

def go_to_grass(player: Player):
    while True:
        route = ask_player_choice(options=route_options, can_go_back=True, prompt="hvilken route?: ")
        if route.lower() == go_back_return:
            break
        wild_pokemon = make_wild_pokemon(routes[route])
        used_pokemon, exp_amout = pokemon_battle(player.team[0], wild_pokemon)
        old_level, new_level = used_pokemon.gain_exp(exp_amout)
        if old_level != new_level:
            print(f"{used_pokemon.name} gikk fra lvl {old_level} -> {new_level}")
        else:
            print(f"{used_pokemon.name} fikk {exp_amout} xp, og totalen er {used_pokemon.exp}")
    

def go_to_pokecenter(player: Player):
    print("pokecenter: all your pokemon are healed")
    for pokemon in player.team:
        pokemon.revive_to_max()

options_info = {
    "grass": go_to_grass,
    "pokecenter": go_to_pokecenter,
}

location_options = list(options_info.keys())

def game_loop(player):
    while True:
        location = ask_player_choice(location_options, "hvor vil du gå?: ")

        location_function = options_info[location]
        clear_screen()
        print(f"du gikk til {location}")

        location_function(player)

game_loop(player)