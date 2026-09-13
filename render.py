import os

def get_hp_bar(pokemon, bar_length=20):
    hp_ratio = pokemon.hp / pokemon.max_hp
    filled = round(hp_ratio * bar_length)
    empty = bar_length - filled
    return "|" + "█" * filled + "_" * empty + "|"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")