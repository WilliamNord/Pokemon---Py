import os
from elements import effectiveness_tekst

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_hp_bar(pokemon: object, bar_length=20):
    hp_ratio = pokemon.hp / pokemon.max_hp
    filled = round(hp_ratio * bar_length)
    empty = bar_length - filled
    return "|" + "█" * filled + "_" * empty + "|"



def battle_text(results: dict) -> list:
    
    if results == {}:
        return [""]
    
    attacker_name = results["attacker"]
    defender_name = results["defender"]
    move_name = results["move_name"]
    effectiveness = results["effectiveness"]
    critical = results["critical"]
    damage = results["damage"]

    text_list = []
    text_list.append(f"{attacker_name} brukte {move_name}\n")
    if effectiveness_tekst(effectiveness) != "":
        text_list.append(f"{move_name} {effectiveness_tekst}")
    if critical:
        text_list.append(f"det var et critical hit!")
    text_list.append(f"{defender_name} tok {damage} damage")
    
    return text_list
    

def render_battle(your_pokemon: object, enemy_pokemon: object, results: dict = {}) -> None:
    """
    Viser den nåværende statusen i en Pokémon-kamp.

    Funksjonen tømmer skjermen og viser navn, HP og HP-bar for både
    spillerens og motstanderens Pokémon. Hvis det er oppgitt en melding,
    vises denne under HP for å informere om hva som skjedde.
    """
    
    text_list = battle_text(results)
    
    for i in range(len(text_list)):
        clear_screen()
        print(f"Battle: {your_pokemon.name} vs {enemy_pokemon.name}")
        print()

        print(f"{your_pokemon.name}: {get_hp_bar(your_pokemon)} {your_pokemon.hp}/{your_pokemon.max_hp} HP")
        print()

        print(f"{enemy_pokemon.name}: {get_hp_bar(enemy_pokemon)} {enemy_pokemon.hp}/{enemy_pokemon.max_hp} HP")
        print()
        
        print(text_list[i])