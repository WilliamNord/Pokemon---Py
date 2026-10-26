import math
import random
import time
from render import render_battle
from elements import check_effectiveness, total_effectiveness
from inputs import ask_player_choice, ask_player_move
import random
from pokemon_class import Pokemon
from player_class import Player
from move_class import Move

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




def attack(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player):
    while True:
        move = ask_player_move(your_pokemon)
        
    pass

def try_catch(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player):
    if player == None:
        print("Det er ingen spiller")
        
    elif player.has_pokeballs == False:
        print("du har ingen pokeballer")
        
    ball_choice = ask_player_choice(player.get_available_pkbls(), "Hvilken ball vil du bruke?: ")

def switch_pokemon(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player):
    pass

def run_away(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player):
    #her kan jeg legge til en sjekk om du klarer å løpe vekk.
    return True

    


# options_info = {
#     "grass": go_to_grass,
#     "pokecenter": go_to_pokecenter,
# }

# location_options = list(options_info.keys())

Battle_options_functions = {
    "attack": attack,
    "catch": try_catch,
    "switch": switch_pokemon,
    "run away": run_away,
}

Battle_options = list(Battle_options_functions.keys())

def player_turn(your_pokemon, enemy_pokemon, player):
    while True:
        render_battle(your_pokemon, enemy_pokemon)
        choice = ask_player_choice(options=Battle_options, prompt="hva vil du gjøre?: ")
        
        result, move = Battle_options_functions[choice](your_pokemon, enemy_pokemon, player)
        
        
        

def pokemon_battle(your_pokemon: Pokemon, enemy_pokemon: Pokemon, player: Player = None) -> tuple[Pokemon, int]:
    #dette er hvor kampen mellom to pokemon blir kalkulert
    """_summary_

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
    
    while not your_pokemon.is_fainted() and not enemy_pokemon.is_fainted():
        render_battle(your_pokemon, enemy_pokemon)
        

        moves_opt = [move for move in your_pokemon.moves]
        
        your_move = ask_player_choice(moves_opt, prompt="hvilket move vil du bruke?: ", can_go_back=True)
        
        render_battle(your_pokemon, enemy_pokemon)
        enemy_move = enemy_pokemon.moves[pick_random_move(enemy_pokemon)]  # midlertidig enemy AI

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
    
    return (your_pokemon, enemy_pokemon.exp_yield())