import math
import random
import time
from render import render_battle, sleep_time
from elements import check_effectiveness, total_effectiveness
from inputs import ask_player_choice, ask_player_move, go_back_return
import random
from pokemon_class import Pokemon
from player_class import Player
from move_class import Move
from pokeball_class import Pokeball

def rnd_dmg_range(floor: int, ceil: int) -> float:
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

def check_if_move_hit(move: Move) -> bool:
    """
    Bruker accuracy-en til {move} til å tilfeldig si om trekket traff eller ikke \n
    Moves som skal ha uendelig accuracy eller fungere uavhengig av det, får en verdi av None og returnerer True
    """
    if move.accuracy == None:
        return True
    
    roll = random.randint(1, 100)
    return roll <= move.accuracy

def check_STAB(pokemon: Pokemon, move: Move) -> float:
    if move.element in pokemon.elements:
        return 1.5
    else:
        return 1.0

def pick_random_move(pokemon: Pokemon):
    return (random.randint(1, len(pokemon.moves)) - 1)

    
def calculate_attack(attacker: Pokemon, defender: Pokemon, used_move: Move) -> dict:
    """
    kalkulerer total dmg gjort mot en annen pokemon med et move
    Kalkulasjonen beregner med physical, special og statur move-kategorier
    """
    move = used_move
    results = {
        "attacker_name": attacker.name,
        "defender_name": defender.name,
        "move_name": move.name,
        "defender_hp_before_hit": defender.hp,
        }
    

    power = move.power
    if move.dmg_category == "physical": 
        attack = attacker.attack
        defence = defender.defence
    elif move.dmg_category == "special":
        attack = attacker.sp_attack
        defence = defender.sp_defence
    elif move.dmg_category == "status":
        results.update({"damage": 0, "effectiveness": 1.0, "critical": False, "move_hit": True})
        return results
    
    level = attacker.level
    
    STAB = check_STAB(attacker, move)
    effectiveness = total_effectiveness(defender, move)
    rnd_dmg_mod = rnd_dmg_range(85, 100)
    critical_hit = is_critical()
    
    level_calc = math.floor((2 * level / 5) + 2)

    core_dmg = math.floor((level_calc * power * attack / defence) / 50) + 2 
    
    if critical_hit:
        core_dmg = math.floor(core_dmg * 1.5)
    
    total_dmg = math.floor(core_dmg * STAB)
    total_dmg = math.floor(total_dmg * effectiveness)
    total_dmg = math.floor(total_dmg * rnd_dmg_mod)
    
    if total_dmg == 0 and effectiveness > 0:
        total_dmg = 1
    
    move_hit = bool
    if check_if_move_hit(move):
        move_hit = True
    else:
        move_hit = False
        total_dmg = 0
    
    results.update({
        "damage": total_dmg,
        "effectiveness": effectiveness,
        "critical": critical_hit,
        "move_hit": move_hit,
        "defender_hp_before_hit": defender.hp,
        })

    return results


def who_goes_first(your_pokemon: Pokemon, enemy_pokemon: Pokemon, your_move: Move, enemy_move: Move) -> Pokemon:
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

def attack(your_pokemon, enemy_pokemon, player):
    render_battle(your_pokemon, enemy_pokemon)
    
    move_opt = [move.name for move in your_pokemon.moves]
    move_name = ask_player_choice(move_opt, True, "Hvilket move vil du bruke?: ")
    
    if move_name == go_back_return:
        return Choice_Results["TURN_NOT_USED"], None
    
    chosen_move_index = move_opt.index(move_name)
    chosen_move = your_pokemon.moves[chosen_move_index]
    return Choice_Results["USED_MOVE"], chosen_move
    

def switch_pokemon(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player = None, can_go_back: bool = True):
    render_battle(your_pokemon, enemy_pokemon)
    if player is None:
        return Choice_Results["POKEMON_SWITCHED"], None
    
    available_pokemon = player.get_remaining_pokemon(current_pokemon=your_pokemon)
    available_pokemon_options = [pokemon.name for pokemon in available_pokemon]
    
    #Spilleren har ikke flere pokemon som er i live. 
    if not available_pokemon:
        print("Du har ingen pokemon du kan bytte til")
        return Choice_Results["TURN_NOT_USED"], None
    
    chosen_pokemon = ask_player_choice(available_pokemon_options, can_go_back, "Hvilken pokemon vil du bytte til?: ")
    
    if chosen_pokemon == go_back_return:
        return Choice_Results["TURN_NOT_USED"], None
    
    pokemon_index = available_pokemon_options.index(chosen_pokemon)
    
    pokemon = available_pokemon[pokemon_index]
    
    return Choice_Results["POKEMON_SWITCHED"], pokemon
    
def calculate_catchvalue(enemy_pokemon: Pokemon, pokeball: Pokeball):
    core = (3 * enemy_pokemon.max_hp - 2*enemy_pokemon.hp)
    status_mod = 1 #Dette er statuser som burn og paralyze som kan påvirke catchrate
    mods = core * enemy_pokemon.catch_rate * pokeball.get_ballmod() * status_mod
    catch_value = mods / (3*enemy_pokemon.max_hp)
    return catch_value

def calculate_catch_shakevalue(catch_value):
    if catch_value >= 255:
        return 65536
    
    mod = (catch_value/255)**0.25
    shakevalue =  int(65536 * mod)
    return shakevalue

def try_catch(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player):
    if player == None:
        print("Det er ingen spiller")
    
    elif player.has_pokeballs == False:
        print("du har ingen pokeballer")
        
    pokeball_tuple_list = player.get_available_pokeballs()
    pokeball_obj_list = []
    pokeball_name_list = []
    pokeball_info_list = []
    for tuple in pokeball_tuple_list:
        pokeball_obj_list.append(tuple[0])
        pokeball_name_list.append(tuple[0].pokeball_type)
        pokeball_info_list.append(tuple[1])
    
    render_battle(your_pokemon, enemy_pokemon)
    ball_choice = ask_player_choice(pokeball_name_list, "Hvilken ball vil du bruke?: ", extra_info=pokeball_info_list)
    
    pokeball = pokeball_obj_list[pokeball_name_list.index(ball_choice)]
    catch_value = calculate_catchvalue(enemy_pokemon, pokeball)
    
    if catch_value >= 255:
        print(f"Du fanget {enemy_pokemon.name} :D")
        player.add_pokemon(enemy_pokemon)
        return Choice_Results["POKEMON_CAUGHT"], enemy_pokemon
    
    
    render_battle(your_pokemon, enemy_pokemon)
    shake_value = calculate_catch_shakevalue(catch_value)
    result, result_obj = pokeball_shake(shake_value, enemy_pokemon)
    
    return result, result_obj

def pokeball_shake(shake_value: int, target_pokemon: Pokemon) -> tuple[str, None] | tuple[str, Pokemon]:
    """Denne funksjonen gjør fire uavhengige sjekker for å se om pokemonen blir fanget eller ikke

    Args:
        shake_value (int): Høyere shake_value => høyere sjangse for å fange
        target_pokemon (Pokemon): Pokemonen som spilleren prøver å fange

    Returns:
        tuple[str, None] | tuple[str, Pokemon]: Resultat string og et resultat objekt
    """
    for i in range(4):
        rand = random.randint(0, 65535)
        time.sleep(sleep_time)
        
        if rand < shake_value:
            print(".", end="", flush=True)
        else:
            print(f"{target_pokemon.name} kom seg ut av ballen :(")
            time.sleep(sleep_time)
            return Choice_Results["TURN_USED"], None
    
    print(f"Du fanget {target_pokemon.name}")
    return Choice_Results["POKEMON_CAUGHT"], target_pokemon

def run_away(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player):
    #her kan jeg legge til en sjekk om du klarer å løpe vekk.
    return Choice_Results["BATTLE_OVER"],  None

def do_attack(attacker: Pokemon, defender: Pokemon, move: Move, your_pokemon, enemy_pokemon):
    results = calculate_attack(attacker, defender, move)
    defender.take_damage(results["damage"])
    render_battle(your_pokemon, enemy_pokemon, results)


def player_turn(your_pokemon, enemy_pokemon, player):
    """Dette er spilleren sin runde hvor de får velge hva de vil gjøre før runden kalkuleres.
    Her skal spilleren kunne velge om de vil angripe, fange, bytte pokemon eller løpe vekk.
    Noen av valgene har i seg selv andre valg.

    Args:
        your_pokemon (Pokemon): Din pokemon
        enemy_pokemon (Pokemon): Enemy pokemon
        player (Player): Spilleren

    Returns:
        Tuple: Returnerer en resultat string og et objekt basser på hva du velger
    """
    while True:
        render_battle(your_pokemon, enemy_pokemon)
        choice = ask_player_choice(Battle_options, False, "Hva vil du gjøre?: ")
        
        result, return_obj = Battle_options_functions[choice](your_pokemon, enemy_pokemon, player)
        
        if result == Choice_Results["TURN_NOT_USED"]:
            #spilleren bruke ikke turen sin
            continue
                    
        return result, return_obj
        

Choice_Results = {
    "USED_MOVE": "used_move",
    "TURN_USED": "turn_used",
    "POKEMON_SWITCHED": "pokemon_switched",
    "TURN_NOT_USED": "turn_not_used",
    "BATTLE_OVER": "battle_over",
    "POKEMON_CAUGHT": "pokemon_caught"
    }

Battle_options_functions = {
    "attack": attack,
    "catch": try_catch,
    "switch": switch_pokemon,
    "run away": run_away,
}

Battle_options = list(Battle_options_functions.keys())

def pokemon_battle(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player = None) -> tuple[Pokemon, int]:
    """
    Dette er funksjonen som simulerer kampen mellom to pokemon, en pokemon og et lag, (eller senere en lag mot et lag)

    Args:
        your_pokemon (Pokemon): Et Pokemon objekt
        enemy_pokemon (Pokemon): Et Pokemon objekt

    Returns:
        tuple [Pokemon, int]:
        Pokemon: Returnerer hvilken pokemon som sist var i kampen
        int: hvor mye exp som den fikk (exp kan være 0 i situasjoner hvor en pokemon løper vekk)
    """
    print("\n")
    print(f"du er i en kamp med {enemy_pokemon.name}")
    ran_away = False
    pokemon_caught = False
    
    battle_ongoing = True
    
    while battle_ongoing and not enemy_pokemon.is_fainted():
        result, return_obj = player_turn(your_pokemon, enemy_pokemon, player)
        
        if result == Choice_Results["BATTLE_OVER"]:
            ran_away = True
            break
        
        if result == Choice_Results["POKEMON_SWITCHED"]:
            your_pokemon = return_obj
        
        if result == Choice_Results["POKEMON_CAUGHT"]:
            pokemon_caught = True
            break
                
        enemy_move = enemy_pokemon.moves[pick_random_move(enemy_pokemon)]  # midlertidig enemy AI

        if result == Choice_Results["USED_MOVE"]:
            your_move = return_obj
            first = who_goes_first(your_pokemon, enemy_pokemon, your_move, enemy_move)
            
            if first == your_pokemon:
                do_attack(your_pokemon, enemy_pokemon, your_move, your_pokemon, enemy_pokemon)
                
                if not enemy_pokemon.is_fainted():
                    do_attack(enemy_pokemon, your_pokemon, enemy_move, your_pokemon, enemy_pokemon)
                else:
                    battle_ongoing = False
            else:
                do_attack(enemy_pokemon, your_pokemon, enemy_move, your_pokemon, enemy_pokemon)

                if not your_pokemon.is_fainted():
                    do_attack(your_pokemon, enemy_pokemon, your_move, your_pokemon, enemy_pokemon)
                else:
                    if player != None:
                        if player.get_remaining_pokemon(your_pokemon):
                            _, return_obj = switch_pokemon(your_pokemon, enemy_pokemon, player, False)
                            your_pokemon = return_obj
        elif result == Choice_Results["TURN_USED"]:
            do_attack(enemy_pokemon, your_pokemon, enemy_move, your_pokemon, enemy_pokemon)

    if ran_away:
        print("Du kom deg unna")
        return your_pokemon, 0
    
    if pokemon_caught:
        print(f"du fanget {enemy_pokemon.name} :D")
        player.add_pokemon(enemy_pokemon)
        return your_pokemon, 0
        
    render_battle(your_pokemon, enemy_pokemon)

    if your_pokemon.is_fainted():
        print(f"Din {your_pokemon.name} tapte mot {enemy_pokemon.name} ")
    else:
        print(f"Hurray! Du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")
    
    return (your_pokemon, enemy_pokemon.exp_yield())