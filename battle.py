import math
import random
import time
from render import render_battle
from elements import check_effectiveness
import random

def rnd_dmg_range(floor, ceil):
    return random.randint(floor, ceil) / 100

def check_STAB(pokemon: object, move: object) -> float:
    if move.element in pokemon.elements:
        return 1.5
    else:
        return 1.0

def effectiveness_tekst(defender: object, move: object) -> str:
    effectiveness = [check_effectiveness(defender, move, 0), check_effectiveness(defender, move, 1)]
    
    sum_effectiveness = effectiveness[0] * effectiveness [1]
    
    match sum_effectiveness:
        case 4:
            return f"{move} er MEGA effektivt!"
        case 2:
            return f"{move} er SUPER effektivt!"
        case 0:
            return f"{move} hadde INGEN effekt!"
        case 1:
            return ""
    
    

def calculate_dmg(attacker: object, defender: object, move: object) -> int:
    """
    kalkulerer total dmg gjort mot en annen pokemon med et move
    Kalkulasjonen beregner med physical, special og statur move-kategorier
    """
    power = move.power
    if move.dmg_category == "physical": 
        attack = attacker.attack
        defence = defender.defence
    elif move.dmg_category == "special":
        attack = attacker.sp_attack
        defence = defender.sp_defence
    elif move.dmg_category == "status":
        return 0
    
    level = attacker.level
    
    STAB = check_STAB(attacker, move)
    element_1 = check_effectiveness(defender, move, 0)
    element_2 = check_effectiveness(defender, move, 1)
    random = rnd_dmg_range(85, 100)
    critical = 1
    core_dmg = math.floor((((2 * level * critical / 5) + 2) * (power * attack / defence) / 50)) + 2
    total_dmg = math.trunc(core_dmg * STAB * element_1 * element_2 * random)
    return total_dmg


def who_goes_first(your_pokemon: object, enemy_pokemon: object, your_move: object, enemy_move: object) -> object:
    #Denne funksjonen bestemmer hvilken pokemon som går først basert på speed og priority
    if your_move.priority > enemy_move.priority:
        return your_pokemon
    elif your_move.priority == enemy_move.priority:
        if your_pokemon.speed > enemy_pokemon.speed:
            return your_pokemon
        else:
            return enemy_pokemon
    else:
        return enemy_pokemon


def ask_player_move(your_pokemon: object) -> object:
    #denne funksjonen spør spilleren om hvilken av alle moves til {your_pokemon} som de vil bruke
    while True:
        print("\n")
        for i, move in enumerate(your_pokemon.moves):
            print(f"{i + 1}. {move.name}")

        try:
            player_choice = int(input("hvilket move vil du bruke?: "))

            if 1 <= player_choice <= len(your_pokemon.moves):
                return your_pokemon.moves[player_choice - 1]
            else:
                print("ERROR: du må velge et move du har")
                time.sleep(sleep_value)

        except ValueError:
            print("du må skrive et tall")
            time.sleep(sleep_value)

sleep_value = 1.5

def pokemon_battle(your_pokemon: object, enemy_pokemon: object) -> None:
    #dette er hvor kampen mellom to pokemon blir kalkulert
    print("\n")
    print(f"du er i en kamp med {enemy_pokemon.name}")
    time.sleep(sleep_value)

    
    while not your_pokemon.is_fainted() and not enemy_pokemon.is_fainted():
        render_battle(your_pokemon, enemy_pokemon,)

        your_move = ask_player_move(your_pokemon)
        enemy_move = enemy_pokemon.moves[0]  # midlertidig enemy AI

        first = who_goes_first(your_pokemon, enemy_pokemon, your_move, enemy_move)

        if first == your_pokemon:
            render_battle(your_pokemon, enemy_pokemon, 
            f"din {your_pokemon.name} brukte {your_move.name}")
            
            time.sleep(sleep_value)

            enemy_damage = calculate_dmg(your_pokemon, enemy_pokemon, your_move)
            enemy_pokemon.take_damage(enemy_damage)
            
            if effectiveness_tekst() == "":
                render_battle(your_pokemon, enemy_pokemon,
                    f"din {your_pokemon.name} brukte {your_move.name}!\n"
                    f"{enemy_pokemon.name} tok {enemy_damage} damage"
                )
            else:
                render_battle(your_pokemon, enemy_pokemon,
                    f"din {your_pokemon.name} brukte {your_move.name}!\n"
                    f"{effectiveness_tekst()}"
                    f"{enemy_pokemon.name} tok {enemy_damage} damage"
                )

            time.sleep(sleep_value)

            if not enemy_pokemon.is_fainted():
                render_battle(your_pokemon, enemy_pokemon, f"{enemy_pokemon.name} brukte {enemy_move.name}")
                time.sleep(sleep_value)

                your_damage = calculate_dmg(enemy_pokemon, your_pokemon, enemy_move)
                your_pokemon.take_damage(your_damage)

                render_battle(
                    your_pokemon,
                    enemy_pokemon,
                    f"{enemy_pokemon.name} brukte {enemy_move.name}\n"
                    f"din {your_pokemon.name} tok {your_damage} damage"
                )
                time.sleep(sleep_value)

        else:
            render_battle(your_pokemon, enemy_pokemon, f"{enemy_pokemon.name} brukte {enemy_move.name}")
            time.sleep(sleep_value)

            your_damage = calculate_dmg(enemy_pokemon, your_pokemon, enemy_move)
            your_pokemon.take_damage(your_damage)

            render_battle(your_pokemon, enemy_pokemon,
                f"{enemy_pokemon.name} brukte {enemy_move.name}\n"
                f"din {your_pokemon.name} tok {your_damage} damage"
            )
            time.sleep(sleep_value)

            if not your_pokemon.is_fainted():
                render_battle(your_pokemon, enemy_pokemon,
                f"din {your_pokemon.name} brukte {your_move.name}")
                
                time.sleep(sleep_value)

                enemy_damage = calculate_dmg(your_pokemon, enemy_pokemon, your_move)
                enemy_pokemon.take_damage(enemy_damage)

                render_battle(your_pokemon, enemy_pokemon,
                    f"din {your_pokemon.name} brukte {your_move.name}\n"
                    f"{enemy_pokemon.name} tok {enemy_damage} damage")
                    
                time.sleep(sleep_value)

    render_battle(your_pokemon, enemy_pokemon, "")

    if your_pokemon.is_fainted():
        print(f"Du tapte mot {enemy_pokemon.name}")
    else:
        print(f"Hurray! Du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")