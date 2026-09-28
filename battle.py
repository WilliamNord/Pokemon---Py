import math
import random
import time
from render import render_battle
from elements import check_effectiveness, total_effectiveness
import random

def rnd_dmg_range(floor, ceil):
    return random.randint(floor, ceil) / 100

def is_critical() -> bool:
    """ 
    Returnerer True eller False basert på en RNG fra 1-24 \n
    1/24: True \n
    23/24: False
    """
    if random.randint(1,24) == 1:
        return True
    else:
        return False

def check_STAB(pokemon: object, move: object) -> float:
    if move.element in pokemon.elements:
        return 1.5
    else:
        return 1.0
    

def calculate_attack(attacker: object, defender: object, move: object) -> dict:
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
        return {"attacker_name": attacker.name,
            "defender_name": defender.name,
            "move_name": move.name,
            "damage": 0,
            "effectiveness": 1.0,
            "critical": False,
            "defender_hp_before_hit": defender.hp,
            }
    
    level = attacker.level
    
    STAB = check_STAB(attacker, move)
    effectiveness = total_effectiveness(defender, move)
    rnd_dmg_mod = rnd_dmg_range(85, 100)
    
    critical_hit = is_critical()
    if critical_hit:
        critical_multiplyer = 1.5
    else:
        critical_multiplyer = 1
        
    core_dmg = math.floor((((2 * level * critical_multiplyer / 5) + 2) * (power * attack / defence) / 50)) + 2
    total_dmg = math.trunc(core_dmg * STAB * effectiveness * rnd_dmg_mod)
    
    results = {
        "attacker_name": attacker.name,
        "defender_name": defender.name,
        "move_name": move.name,
        "damage": total_dmg,
        "effectiveness": effectiveness,
        "critical": critical_hit,
        "defender_hp_before_hit": defender.hp,
    }
    return results


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
    """ 
    denne funksjonen spør spilleren om hvilken av alle moves til dere pokemon som de vil bruke
    """
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
        render_battle(your_pokemon, enemy_pokemon)

        your_move = ask_player_move(your_pokemon)
        enemy_move = enemy_pokemon.moves[0]  # midlertidig enemy AI

        first = who_goes_first(your_pokemon, enemy_pokemon, your_move, enemy_move)

        if first == your_pokemon:
            attack_results = calculate_attack(your_pokemon, enemy_pokemon, your_move)
            enemy_damage = attack_results["damage"]
            enemy_pokemon.take_damage(enemy_damage)

            render_battle(your_pokemon, enemy_pokemon, attack_results)
            
            if not enemy_pokemon.is_fainted():
                attack_results = calculate_attack(enemy_pokemon, your_pokemon, enemy_move)
                your_damage = attack_results["damage"]
                your_pokemon.take_damage(your_damage)
                
                render_battle(your_pokemon, enemy_pokemon, attack_results)
        else:
            
            attack_results = calculate_attack(enemy_pokemon, your_pokemon, enemy_move)
            your_damage = attack_results["damage"]
            your_pokemon.take_damage(your_damage)
            
            render_battle(your_pokemon, enemy_pokemon, attack_results)

            if not your_pokemon.is_fainted():
                
                attack_results = calculate_attack(your_pokemon, enemy_pokemon, your_move)
                enemy_damage = attack_results["damage"]
                enemy_pokemon.take_damage(enemy_damage)

                render_battle(your_pokemon, enemy_pokemon, attack_results)

    render_battle(your_pokemon, enemy_pokemon)

    if your_pokemon.is_fainted():
        print(f"Du tapte mot {enemy_pokemon.name}")
    else:
        print(f"Hurray! Du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")