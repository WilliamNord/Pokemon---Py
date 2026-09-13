# class Person:
#     def __init__(self, name: str, age:int , fav_color: str):
#         self.name = name
#         self.fav_color = fav_color
#         self.age = age
    
#     def hilsen(self):
#         print(f"jeg hater {self.name}, jeg er {self.age} år gammer og jeg liker fargen {self.fav_color}")
        
# john = Person("john", 48, "Blue")
# hilde = Person("hilde", 26, "Grønn")
# john.hilsen()
# hilde.hilsen()

#metode for super effektive typer
elementer = {
    "fire": {
        "strong": ["ice", "grass", "metal", "bug"],
        "weak": ["ground", "water", "rock",],
        },
    "water": {
        "strong": ["fire", "ground","electric"],
        "weak": ["grass", "electric"],
    }
}

print(elementer["fire"]["strong"][0])


import math
import time
from move_class import Move
from pokemon_class import Pokemon
from move_bank import *

    
def calculate_dmg(attacker, defender, move):
    power = move.power
    attack = attacker.attack
    defence = defender.defence
    level = 10 
    critical = 1
    total_dmg = (((2*level*critical / 5) +2) * (power * attack/defence) / 50) + 2
    total_dmg = math.ceil(total_dmg)
    return total_dmg
    

charizard = Pokemon("charizard", "fire", 100, 70, 90, 70, 50, 65, [flamethrower, scratch, gun])
bulbasaur = Pokemon("bulbasaur", "grass", 45, 49, 49, 65, 65, 45, [grass_knot, scratch])
testmon = Pokemon("testmon", "test_element", 1,1,1,1,1,1)

# charizard.take_damage(50)

# charizard.take_damage(20)
# charizard.take_damage(10)
# charizard.take_damage(0.5)
# charizard.take_damage(0.05)


charizard.talk()
bulbasaur.talk()
testmon.talk()


your_pokemon = charizard
enemy_pokemon = bulbasaur

buffer_time = 0.8

def battle(your_pokemon, enemy_pokemon):
    print("\n \n")
    print(f"du er i en kamp med {enemy_pokemon.name}")
    
    while not your_pokemon.is_fainted() and not enemy_pokemon.is_fainted():
        
        #kode for å spørre spilleren om hvilken move de vil bruke
        move_is_chosen = False
        while move_is_chosen == False:
            print("\n")
            for i, move in enumerate(your_pokemon.moves):
                print(f"{i + 1}. {move.name}")
                
            player_choice = int(input(f"hvilken move vil du bruke?: "))
            if 0 <= player_choice > len(your_pokemon.moves):
                print("ERROR: du må skrive tallet til et move du har!")
                time.sleep(1)
            else:
                move_is_chosen = True
                
            print("\n")
        
        your_move = your_pokemon.moves[player_choice - 1]
        #må senere oppdatere enemy AI
        enemy_move = enemy_pokemon.moves[1]
        
        time.sleep(buffer_time)
        print("du brukte:", your_pokemon.moves[player_choice - 1].name)
        
        #hvis du er raskest og bruker det raskeste eller like raskt move som enemy_mon
        #må senere legge til tilfeldig sjangse for hvem som går først med lik pokemon.speed
        #i spillene skal det være 50 50
        if your_pokemon.speed > enemy_pokemon.speed and your_move.priority >= enemy_move.priority:
            time.sleep(buffer_time)
            print("du er raskest")
            print(f"{your_pokemon.name} brukte {your_move.name} på {enemy_pokemon.name}")
            
            time.sleep(buffer_time)
            enemy_pokemon.take_damage(calculate_dmg(your_pokemon, enemy_pokemon, your_move))
            
            if enemy_pokemon.is_fainted() == False:
                time.sleep(buffer_time)
                your_pokemon.take_damage(calculate_dmg(enemy_pokemon, your_pokemon, enemy_move))
        
        else:
            print("enemy pokemon er raskest")
            time.sleep(buffer_time)
            print(f"{enemy_pokemon.name} brukte {enemy_move.name} på din {your_pokemon.name}")
            
            time.sleep(buffer_time)
            your_pokemon.take_damage(calculate_dmg(enemy_pokemon, your_pokemon, enemy_move))
            
            if your_pokemon.is_fainted() == False:
                time.sleep(buffer_time)
                enemy_pokemon.take_damage(calculate_dmg(your_pokemon, enemy_pokemon, your_move))
    
        time.sleep(buffer_time)
    
    if your_pokemon.is_fainted() == True:
        print(f"Du tapte mot {enemy_pokemon.name}")
    elif enemy_pokemon.is_fainted() == True:
        print("\n")
        print(f"hurray du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")
        
    
battle(your_pokemon, enemy_pokemon)
