import math
import time
from render import render_battle

def calculate_dmg(attacker, defender, move):
    power = move.power
    attack = attacker.attack
    defence = defender.defence
    level = 10
    critical = 1
    total_dmg = (((2 * level * critical / 5) + 2) * (power * attack / defence) / 50) + 2
    total_dmg = math.ceil(total_dmg)
    return total_dmg


def who_goes_first(your_pokemon, enemy_pokemon, your_move, enemy_move):
    if your_move.priority > enemy_move.priority:
        return your_pokemon
    elif your_move.priority == enemy_move.priority:
        if your_pokemon.speed > enemy_pokemon.speed:
            return your_pokemon
        else:
            return enemy_pokemon
    else:
        return enemy_pokemon


def ask_player_move(your_pokemon):
    while True:
        print("\n")
        for i, move in enumerate(your_pokemon.moves):
            print(f"{i + 1}. {move.name} {j}")

        try:
            player_choice = int(input("hvilket move vil du bruke?: "))

            if 1 <= player_choice <= len(your_pokemon.moves):
                return your_pokemon.moves[player_choice - 1]
            else:
                print("ERROR: du må velge et move du har")
                time.sleep(1)

        except ValueError:
            print("du må skrive et tall")
            time.sleep(1)



def pokemon_battle(your_pokemon, enemy_pokemon):
    print("\n")
    print(f"du er i en kamp med {enemy_pokemon.name}")
    time.sleep(1)

    
    while not your_pokemon.is_fainted() and not enemy_pokemon.is_fainted():
        render_battle(your_pokemon, enemy_pokemon,)

        your_move = ask_player_move(your_pokemon)
        enemy_move = enemy_pokemon.moves[0]  # midlertidig AI

        first = who_goes_first(your_pokemon, enemy_pokemon, your_move, enemy_move)

        if first == your_pokemon:
            render_battle(your_pokemon, enemy_pokemon, f"{your_pokemon.name} brukte {your_move.name}!")
            time.sleep(1)

            enemy_damage = calculate_dmg(your_pokemon, enemy_pokemon, your_move)
            enemy_pokemon.take_damage(enemy_damage)

            render_battle(your_pokemon, enemy_pokemon,
                f"{your_pokemon.name} brukte {your_move.name}!\n"
                f"{enemy_pokemon.name} tok {enemy_damage} damage!"
            )
            time.sleep(1)

            if not enemy_pokemon.is_fainted():
                render_battle(your_pokemon, enemy_pokemon, f"{enemy_pokemon.name} brukte {enemy_move.name}!")
                time.sleep(1)

                your_damage = calculate_dmg(enemy_pokemon, your_pokemon, enemy_move)
                your_pokemon.take_damage(your_damage)

                render_battle(
                    your_pokemon,
                    enemy_pokemon,
                    f"{enemy_pokemon.name} brukte {enemy_move.name}!\n"
                    f"{your_pokemon.name} tok {your_damage} damage!"
                )
                time.sleep(1)

        else:
            render_battle(your_pokemon, enemy_pokemon, f"{enemy_pokemon.name} brukte {enemy_move.name}!")
            time.sleep(1)

            your_damage = calculate_dmg(enemy_pokemon, your_pokemon, enemy_move)
            your_pokemon.take_damage(your_damage)

            render_battle(your_pokemon, enemy_pokemon,
                f"{enemy_pokemon.name} brukte {enemy_move.name}!\n"
                f"{your_pokemon.name} tok {your_damage} damage!"
            )
            time.sleep(1)

            if not your_pokemon.is_fainted():
                render_battle(your_pokemon, enemy_pokemon, f"{your_pokemon.name} brukte {your_move.name}!")
                time.sleep(1)

                enemy_damage = calculate_dmg(your_pokemon, enemy_pokemon, your_move)
                enemy_pokemon.take_damage(enemy_damage)

                render_battle(your_pokemon, enemy_pokemon,
                    f"{your_pokemon.name} brukte {your_move.name}!\n"
                    f"{enemy_pokemon.name} tok {enemy_damage} damage!")
                    
                time.sleep(1)

    render_battle(your_pokemon, enemy_pokemon, "")

    if your_pokemon.is_fainted():
        print(f"Du tapte mot {enemy_pokemon.name}")
    else:
        print(f"Hurray! Du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")