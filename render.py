import os
from elements import elementer

def get_hp_bar(pokemon, bar_length=20):
    hp_ratio = pokemon.hp / pokemon.max_hp
    filled = round(hp_ratio * bar_length)
    empty = bar_length - filled
    return "|" + "█" * filled + "_" * empty + "|"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def render_battle(your_pokemon, enemy_pokemon, your_move, enemy_move, first):
    clear_screen()
    
    print(f"Battle: {enemy_pokemon.name} vs {your_pokemon.name} \n")
    
    your_message = f"{your_pokemon.name} brukte {your_move.name} på {enemy_pokemon.name}"
    enemy_message = f"{enemy_pokemon.name} brukte {enemy_move.name} på {enemy_pokemon.name}"
    
    first_message = None
    last_message = None
    
    if first == your_pokemon:
        first_message = your_message
        last_message = enemy_message
    else:
        first_message = enemy_message
        last_message = your_message
    
    effectiveness = ""
    
    try:
        if enemy_pokemon.element in elementer[your_move.element]["strong"]:
            effectiveness = f"det er super effectivt"
    except KeyError:
        print("ERROR: en feil skjedde i render.py")

    if your_pokemon.fainted == False:
        print(first_message, effectiveness) 
    if enemy_pokemon.fainted == False:
        print(last_message)
        
    print()
    
    print(f"{enemy_pokemon.name}: {get_hp_bar(enemy_pokemon)} {enemy_pokemon.hp}/{enemy_pokemon.max_hp} HP")
    print()


    print(f"{your_pokemon.name}: {get_hp_bar(your_pokemon)} {your_pokemon.hp}/{your_pokemon.max_hp} HP")
    print()