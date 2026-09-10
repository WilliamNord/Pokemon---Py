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


class Pokemon:
    def __init__(self, name: str, element: str, hp:int, defence: int, attack: int, sp_attack: int, sp_defence: int, speed: int, moves = None, fainted = False):
        self.name = name
        self.element = element
        self.hp = hp
        self.max_hp = hp
        self.defence = defence
        self.attack = attack
        self.sp_attack = sp_attack
        self.sp_defence = sp_defence
        self.speed = speed
        
        if moves is None:
            self.moves = [scratch]
        else:
            self.moves = moves
            
        self.fainted = False
    
    def talk(self):
        print(f"jeg er {self.name}")
        print(f"jeg har {self.defence} defence og {self.attack} attack")
        
        print("jeg har trekk som:")
        for move in self.moves:
            print(move.name)
    
    def take_damage(self, incoming_damage):
        self.hp -= math.ceil(int(incoming_damage))
        if self.hp <= 0:
            self.hp = 0
            self.fainted = True
        
        hp_persent = round((self.hp / self.max_hp)*100, 2)
        print(f"{self.name} took {incoming_damage} damage and has {self.hp} hp remaining ({hp_persent}% remaining")
    
    def is_fainted(self):
        if self.hp <= 0:
            self.fainted = True
            return True
        else:
            return False


class Move():
    def __init__(self, name: str , element: str, power: int, accuracy: int, priority: int):
        self.name = name
        self.element = element
        self.power = power
        self.accuracy = accuracy
        self.priority = priority
    
def calculate_dmg(attacker, defender, move):
    power = move.power
    attack = attacker.attack
    defence = defender.defence
    level = 10 
    critical = 1
    total_dmg = (((2*level*critical / 5) +2) * (power * attack/defence) / 50) + 2
    total_dmg = math.ceil(total_dmg)
    return total_dmg
    
scratch = Move("scratch", "normal", 10, 100, 1)
flamethrower = Move("flamethrower", "fire", 70, 100, 0)
grass_knot = Move("grass knot", "grass", 60, 100, 1)

charizard = Pokemon("charizard", "fire", 100, 70, 90, 70, 50, 65, [flamethrower, scratch])
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
            
            for i, move in enumerate(your_pokemon.moves):
                print(f"{i + 1}. {move.name}")
                
            player_choice = int(input(f"hvilken move vil du bruke?: "))
            if 0 <= player_choice > len(your_pokemon.moves):
                print("ERROR: du må skrive tallet til et move du har!")
                time.sleep(1)
            else:
                move_is_chosen = True
        
        your_move = your_pokemon.moves[player_choice - 1]
        enemy_move = enemy_pokemon.moves[0]
        
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
            print(f"{enemy_pokemon.name} brukte {enemy_move.name} på din {your_pokemon.name}")
            
            time.sleep(buffer_time)
            your_pokemon.take_damage(calculate_dmg(enemy_pokemon, your_pokemon, enemy_move))
            
            if your_pokemon.is_fainted() == False:
                time.sleep(buffer_time)
                enemy_pokemon.take_damage(calculate_dmg(your_pokemon, enemy_pokemon, your_move))
                
    if your_pokemon.is_fainted() == True:
        print(f"Du tapte mot {enemy_pokemon.name}")
    elif enemy_pokemon.is_fainted() == True:
        print("\n")
        print(f"hurray du vant mot {enemy_pokemon.name} med din {your_pokemon.name}")
        
    
battle(your_pokemon, enemy_pokemon)

# while True:
#     # attack_opt = input(f"hva vil du angripe med?\n 1 {flamethrower}")
#     # enemy_attack_opt = enemy_move_calc_func
#     # if your_pokemon.speed > enemy_pokemon.speed:
#     #     print(f"{your_pokemon.name} går først")
#     # else:
#     #     print(f"{enemy_pokemon.name} går først")


#kode for om du har lyst til å angripe eller løpe vekk:

# print(f"du er i en kamp med en {enemy_pokemon}")
# battle_start_opt = input("hva vil du gjøre? 1: attack, 2: run away \n")

# match battle_start_opt:
#     case "1":
#         print("battle is started")