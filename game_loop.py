from inputs import ask_player_location
from player_class import Player

player = Player("John pokemon")

def go_to_grass(player):
    print("this is grass")

def go_to_pokecenter(player):
    print("pokecenter")

options_info = {
    "grass": go_to_grass,
    "pokecenter": go_to_pokecenter,
}

options = list(options_info.keys())

def game_loop(player):
    while True:
        location = ask_player_location(options)

        location_function = options_info[location]

        location_function(player)

game_loop(player)