from move_class import Move
import math

scratch = Move("scratch", "normal", 10, 100, 0)

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
        print(f"{self.name} tok {incoming_damage} damage og har {self.hp} hp igjen ({hp_persent})% remaining")
    
    def is_fainted(self):
        if self.hp <= 0:
            self.fainted = True
            return True
        else:
            return False