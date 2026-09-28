import os
import time
from elements import effectiveness_tekst

sleep_time = 1.5



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_hp_bar(pokemon: object, bar_length=20):
    hp_ratio = pokemon.hp / pokemon.max_hp
    filled = round(hp_ratio * bar_length)
    empty = bar_length - filled
    return "|" + "█" * filled + "_" * empty + "|"



def battle_text(results: dict) -> list:
    
    if not results:
        return []
    
    attacker_name = results["attacker_name"]
    defender_name = results["defender_name"]
    move_name = results["move_name"]
    total_effectiveness = results["effectiveness"]
    critical = results["critical"]
    damage = results["damage"]

    text_list = []
    text_list.append(f"{attacker_name} brukte {move_name}\n")
    if effectiveness_tekst(total_effectiveness) != "":
        text_list.append(f"{move_name} {effectiveness_tekst(total_effectiveness)}")
    if critical:
        text_list.append(f"det var et critical hit!")
    text_list.append(f"{defender_name} tok {damage} damage")
    
    return text_list
    

import os
import time
from elements import effectiveness_tekst


sleep_time = 1.5


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_hp_bar(pokemon: object, hp: int = None, bar_length=20):
    if hp is None:
        hp = pokemon.hp
    
    hp_ratio = hp / pokemon.max_hp
    filled = round(hp_ratio * bar_length)
    empty = bar_length - filled

    return "|" + "█" * filled + "_" * empty + "|"


def battle_text(results):
    if not results:
        return []

    attacker_name = results["attacker_name"]
    defender_name = results["defender_name"]
    move_name = results["move_name"]
    effectiveness = results["effectiveness"]
    critical = results["critical"]
    damage = results["damage"]

    text_list = []

    text_list.append(
        f"{attacker_name} brukte {move_name}"
    )

    effectiveness_text = effectiveness_tekst(effectiveness)

    if effectiveness_text:
        text_list.append(f"{move_name} er {effectiveness_text}")

    if critical:
        text_list.append("critical hit")

    text_list.append(
        f"{defender_name} tok {damage} damage"
    )

    return text_list


def render_battle(your_pokemon, enemy_pokemon, results=None):
    """
    Viser den nåværende statusen i en Pokémon-kamp.

    Funksjonen tømmer skjermen og viser navn, HP og HP-bar for både
    spillerens og motstanderens Pokémon. Hvis det er oppgitt en melding,
    vises denne under HP for å informere om hva som skjedde.
    """
    text_list = battle_text(results)
    old_text = []

    your_hp = your_pokemon.hp
    enemy_hp = enemy_pokemon.hp
    
    if not text_list:
        clear_screen()

        print(f"Battle: {your_pokemon.name} vs {enemy_pokemon.name}")
        print()

        print(f"{your_pokemon.name}: {get_hp_bar(your_pokemon)} {your_hp}/{your_pokemon.max_hp} HP")
        print()

        print(f"{enemy_pokemon.name}: {get_hp_bar(enemy_pokemon)} {enemy_hp}/{enemy_pokemon.max_hp} HP")
        print()
        
        return

    # Viser én ny melding om gangen
    for index, text in enumerate(text_list):
        old_text.append(text)

        # her prøver jeg å oppdatere HP bare når "tok damage" teksten vises
        if index < len(text_list) - 1:
            your_hp = your_pokemon.hp
            enemy_hp = enemy_pokemon.hp

            if results["defender_name"] == your_pokemon.name:
                your_hp = results["defender_hp_before_hit"]

            elif results["defender_name"] == enemy_pokemon.name:
                enemy_hp = results["defender_hp_before_hit"]
        
        # På siste melding, altså "tok damage":
        # bruk den nye HP-en
        else:
            your_hp = your_pokemon.hp
            enemy_hp = enemy_pokemon.hp
                
        clear_screen()

        print(f"Battle: {your_pokemon.name} vs {enemy_pokemon.name}")
        print()

        print(f"{your_pokemon.name}: {get_hp_bar(your_pokemon, your_hp)} {your_hp}/{your_pokemon.max_hp} HP")
        print()

        print(f"{enemy_pokemon.name}: {get_hp_bar(enemy_pokemon, enemy_hp)} {enemy_hp}/{enemy_pokemon.max_hp} HP")
        print()

        for message in old_text:
            print(message)

        time.sleep(sleep_time)