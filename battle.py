import math
import time
from render import render_battle

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
    else:
        return 0
        
    level = 10
    critical = 1
    total_dmg = (((2 * level * critical / 5) + 2) * (power * attack / defence) / 50) + 2
    total_dmg = math.ceil(total_dmg)
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
            render_battle(your_pokemon, enemy_pokemon, f"din {your_pokemon.name} brukte {your_move.name}!")
            time.sleep(sleep_value)

            enemy_damage = calculate_dmg(your_pokemon, enemy_pokemon, your_move)
            enemy_pokemon.take_damage(enemy_damage)

            render_battle(your_pokemon, enemy_pokemon,
                f"din {your_pokemon.name} brukte {your_move.name}!\n"
                f"{enemy_pokemon.name} tok {enemy_damage} damage!"
            )
            time.sleep(sleep_value)

            if not enemy_pokemon.is_fainted():
                render_battle(your_pokemon, enemy_pokemon, f"{enemy_pokemon.name} brukte {enemy_move.name}!")
                time.sleep(sleep_value)

                your_damage = calculate_dmg(enemy_pokemon, your_pokemon, enemy_move)
                your_pokemon.take_damage(your_damage)

                render_battle(
                    your_pokemon,
                    enemy_pokemon,
                    f"{enemy_pokemon.name} brukte {enemy_move.name}!\n"
                    f"din {your_pokemon.name} tok {your_damage} damage!"
                )
                time.sleep(sleep_value)

        else:
            render_battle(your_pokemon, enemy_pokemon, f"{enemy_pokemon.name} brukte {enemy_move.name}!")
            time.sleep(sleep_value)

            your_damage = calculate_dmg(enemy_pokemon, your_pokemon, enemy_move)
            your_pokemon.take_damage(your_damage)

            render_battle(your_pokemon, enemy_pokemon,
                f"{enemy_pokemon.name} brukte {enemy_move.name}!\n"
                f"din {your_pokemon.name} tok {your_damage} damage!"
            )
            time.sleep(sleep_value)

            if not your_pokemon.is_fainted():
                render_battle(your_pokemon, enemy_pokemon,
                f"din {your_pokemon.name} brukte {your_move.name}!")
                
                time.sleep(sleep_value)

                enemy_damage = calculate_dmg(your_pokemon, enemy_pokemon, your_move)
                enemy_pokemon.take_damage(enemy_damage)

                render_battle(your_pokemon, enemy_pokemon,
                    f"din {your_pokemon.name} brukte {your_move.name}!\n"
                    f"{enemy_pokemon.name} tok {enemy_damage} damage!")
                    
                time.sleep(sleep_value)

    render_battle(your_pokemon, enemy_pokemon, "")

    if your_pokemon.is_fainted():
        print(f"Du tapte mot {enemy_pokemon.name}")
    else:
        print(f"Hurray! Du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")