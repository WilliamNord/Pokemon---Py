from move_bank import scratch
import math

#Klassen for pokemon objekter
class Pokemon:
    def __init__(self, name: str, element_1: str, element_2: str, hp: int, attack: int, defence: int, sp_attack: int, sp_defence: int, speed: int, moves = None, level = 100, fainted = False):
        self.name = name
        self.element_1 = element_1
        self.element_2 = element_2
        self.base_stats = {
                "hp": hp,
                "attack": attack,
                "defence": defence,
                "sp_attack": sp_attack,
                "sp_defence": sp_defence,
                "speed": speed,
            }
        
        self.level = level
        
        if moves is None:
            self.moves = [scratch]
        else:
            self.moves = moves
            
        self.fainted = False
        
        #individual values
        #skal genereres ved laging av pokemon
        self.IVs = {
            "hp": 0,
            "attack": 0,
            "defence": 0,
            "sp_attack": 0,
            "sp_defence": 0,
            "speed": 0,
        }
        
        #effort values
        #økes via spilling
        self.EVs = {
            "hp": 0,
            "attack": 0,
            "defence": 0,
            "sp_attack": 0,
            "sp_defence": 0,
            "speed": 0,
        }
        
        self.calculate_all_stats()
        self.hp = self.max_hp

    
    #HP kalkuleres litt annerledes enn alle andre stats
    def calculate_stat(self, stat_name: str):
        base_stat = self.base_stats[stat_name]
        EVs = self.EVs[stat_name]
        IVs = self.IVs[stat_name]
        
        match stat_name:
            case "hp":
                return math.floor(((2 * base_stat + IVs + math.floor(EVs / 4)) * self.level) / 100) + self.level + 10
            case _:
                return math.floor(((2 * base_stat + IVs + math.floor(EVs / 4)) * self.level) / 100) + 5
    
    def calculate_all_stats(self):
        """
        denne funksjonen kalkulerer alle stats til en pokemon.
        """
        self.max_hp = self.calculate_stat("hp")
        self.attack = self.calculate_stat("attack")
        self.defence = self.calculate_stat("defence")
        self.sp_attack = self.calculate_stat("sp_attack")
        self.sp_defence = self.calculate_stat("sp_defence")
        self.speed = self.calculate_stat("speed")
    
    def talk(self):
        print(f"jeg er {self.name}")
        print(f"jeg har {self.defence} defence og {self.attack} attack")
        
        print("jeg har trekk som:")
        for move in self.moves:
            print(move.name)
    
    def take_damage(self, incoming_damage: int) -> None:
        self.hp -= int(incoming_damage)
        if self.hp <= 0:
            self.hp = 0
            self.fainted = True
        
    
    def is_fainted(self):
        if self.hp <= 0:
            self.fainted = True
            return True
        else:
            return False
    
    