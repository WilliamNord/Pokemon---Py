from move_bank import scratch

#Klassen for pokemon objekter
class Pokemon:
    def __init__(self, name: str, element_1: str, element_2: str, hp: int, attack: int, defence: int, sp_attack: int, sp_defence: int, speed: int, moves = None, fainted = False):
        self.name = name
        self.element_1 = element_1
        self.element_2 = element_2
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