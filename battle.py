import math
from render import render_battle

def calculate_dmg(attacker, defender, move):
    power = move.power
    attack = attacker.attack
    defence = defender.defence
    level = 10 
    critical = 1
    total_dmg = (((2*level*critical / 5) +2) * (power * attack/defence) / 50) + 2
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


def pokemon_battle(your_pokemon, enemy_pokemon):
    print("\n")
    print(f"du er i en kamp med {enemy_pokemon.name}")
    
    while not your_pokemon.is_fainted() and not enemy_pokemon.is_fainted():
        
        #kode for å spørre spilleren om hvilken move de vil bruke
        move_is_chosen = False
        while move_is_chosen == False:
            print("\n")
            for i, move in enumerate(your_pokemon.moves):
                print(f"{i + 1}. {move.name}")
            
            #input fra spiller
            try:
                player_choice = int(input(f"hvilken move vil du bruke?: "))
                
                if 1 <= player_choice <= len(your_pokemon.moves):
                    move_is_chosen = True
                else:
                    print("ERROR: du må velge et move du har")
            except ValueError:
                print("du må skrive et tall")    
                
            print("\n")
        
        your_move = your_pokemon.moves[player_choice - 1]
        
        #må senere oppdatere enemy AI
        enemy_move = enemy_pokemon.moves[0]
        
        print("du brukte:", your_pokemon.moves[player_choice - 1].name)
        
        #hvis du er raskest og bruker det raskeste eller like raskt move som enemy_mon
        #må senere legge til tilfeldig sjangse for hvem som går først med lik pokemon.speed
        #i spillene skal det være 50 50
        if who_goes_first(your_pokemon, enemy_pokemon, your_move, enemy_move) == your_pokemon:
            print("du er raskest")
            
            enemy_pokemon.take_damage(calculate_dmg(your_pokemon, enemy_pokemon, your_move))
            
            if enemy_pokemon.is_fainted() == False:
                your_pokemon.take_damage(calculate_dmg(enemy_pokemon, your_pokemon, enemy_move))
            
            render_battle(your_pokemon, enemy_pokemon, your_move, enemy_move, your_pokemon)
        
        else:
            print("enemy pokemon er raskest")
            
            your_pokemon.take_damage(calculate_dmg(enemy_pokemon, your_pokemon, enemy_move))
            
            if your_pokemon.is_fainted() == False:
                enemy_pokemon.take_damage(calculate_dmg(your_pokemon, enemy_pokemon, your_move))
            
            render_battle(your_pokemon, enemy_pokemon, your_move, enemy_move, your_pokemon)
    
    if your_pokemon.is_fainted() == True:
        print(f"Du tapte mot {enemy_pokemon.name}")
    elif enemy_pokemon.is_fainted() == True:
        print("\n")
        print(f"hurray du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")