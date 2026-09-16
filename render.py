import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_hp_bar(pokemon, bar_length=20):
    hp_ratio = pokemon.hp / pokemon.max_hp
    filled = round(hp_ratio * bar_length)
    empty = bar_length - filled
    return "|" + "█" * filled + "_" * empty + "|"


def render_battle(your_pokemon, enemy_pokemon, message=""):
    clear_screen()

    print(f"Battle: {enemy_pokemon.name} vs {your_pokemon.name}")
    print()

    print(f"{your_pokemon.name}: {get_hp_bar(your_pokemon)} {your_pokemon.hp}/{your_pokemon.max_hp} HP")
    print()
    
    print(f"{enemy_pokemon.name}: {get_hp_bar(enemy_pokemon)} {enemy_pokemon.hp}/{enemy_pokemon.max_hp} HP")
    print()

    
    if message != "":
        print(message)
        print()