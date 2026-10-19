import os
import time
from elements import effectiveness_tekst, all_elements
from pokemon_class import Pokemon
from move_class import Move


sleep_time = 1.5


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_hp_bar(pokemon: Pokemon, hp: int | None = None, bar_length: int=20):
    if hp is None:
        hp = pokemon.hp
    
    hp_ratio = hp / pokemon.max_hp
    filled = round(hp_ratio * bar_length)
    empty = bar_length - filled

    return "|" + "█" * filled + "_" * empty + "|"


def battle_text(results):
    if results == None:
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
    if results["move_hit"] == False:
        text_list.append(f"{results['move_name']} bommet!")
        return text_list

    effectiveness_text = effectiveness_tekst(effectiveness)

    if effectiveness_text:
        text_list.append(f"{move_name} er {effectiveness_text}")

    if critical:
        text_list.append("critical hit!")

    text_list.append(
        f"{defender_name} tok {damage} damage"
    )

    return text_list

def draw_hp_bars(your_pokemon: Pokemon, enemy_pokemon: Pokemon, your_hp, enemy_hp):
    
    your_elmt1 = all_elements[your_pokemon.element_1]["short_name"]
    your_elmt2 = all_elements[your_pokemon.element_2]["short_name"]
    enemy_elmt1 = all_elements[enemy_pokemon.element_1]["short_name"]
    enemy_elmt2 = all_elements[enemy_pokemon.element_2]["short_name"]
    your_elements: str
    if your_elmt2 != None:
        your_elements = f"[{your_elmt1}][{your_elmt2}]"
    else:
        your_elements = f"[{your_elmt1}]"
    
    if enemy_elmt2 != None:
        enemy_elements = f"[{enemy_elmt1}][{enemy_elmt2}]"
    else:
        enemy_elements = f"[{enemy_elmt1}]"
        
    
    print(f"Battle: {your_pokemon.name} vs {enemy_pokemon.name}")
    print()

    print(f"{your_pokemon.name} {your_elements} (L:{your_pokemon.level}): {get_hp_bar(your_pokemon)} {your_hp}/{your_pokemon.max_hp} HP")
    print()

    print(f"{enemy_pokemon.name} {enemy_elements} (L:{enemy_pokemon.level}): {get_hp_bar(enemy_pokemon)} {enemy_hp}/{enemy_pokemon.max_hp} HP")
    print()


def render_battle(your_pokemon: Pokemon, enemy_pokemon: Pokemon, results=None):
    """
    Viser den nåværende statusen i en Pokémon-kamp.

    Funksjonen tømmer skjermen og viser navn, HP og HP-bar for både
    spillerens og motstanderens Pokémon. Hvis det er oppgitt en melding,
    vises denne under HP for å informere om hva som skjedde.
    """
    your_hp = your_pokemon.hp
    enemy_hp = enemy_pokemon.hp
    
    if results == None:
        clear_screen()
        
        draw_hp_bars(your_pokemon, enemy_pokemon, your_hp, enemy_hp)
        
        return
    else:
        text_list = battle_text(results)
        old_text = []
        
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
            
            else:
                your_hp = your_pokemon.hp
                enemy_hp = enemy_pokemon.hp
                    
            clear_screen()

            draw_hp_bars(your_pokemon, enemy_pokemon, your_hp, enemy_hp)

            for message in old_text:
                print(message)

            time.sleep(sleep_time)
        
