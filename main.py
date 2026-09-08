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


class Pokemon:
    def __init__(self, name: str, element: str, hp:int, defense: int, attack: int, sp_attack: int, sp_defense: int, speed: int, moves=None, fainted = False):
        self.name = name
        self.element = element
        self.hp = hp
        self.max_hp = hp
        self.defense = defense
        self.attack = attack
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        
        if moves is None:
            self.moves = [scratch]
        else:
            self.moves = moves
            
        self.fainted = False
    
    def talk(self):
        print(f"jeg er {self.name}")
        print(f"jeg har {self.defense} defense og {self.attack} attack")
        
        print("jeg har trekk som:")
        for move in self.moves:
            print(move.name)
    
    def take_damage(self, incoming_damage):
        self.hp -= int(incoming_damage)
        if self.hp <= 0:
            self.hp = 0
            self.fained = True
        print(f"{self.name} took {incoming_damage} and has {self.hp}hp remaining")
    
    def is_fainted(self):
        if self.hp <= 0:
            self.fained = True
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
    
    
scratch = Move("scratch", "normal", 10, 100, 1)
flamethrower = Move("flamethrower", "fire", 70, 100, 0)
grass_knot = Move("grass knot", "grass", 60, 100, 1)

charizard = Pokemon("charizard", "fire", 100, 70, 90, 70, 50, 65, [scratch, flamethrower])
bulbasaur = Pokemon("bulbasaur", "grass", 45, 49, 49, 65, 65, 45, [scratch, grass_knot])
testmon = Pokemon("testmon", "test_element", 1,1,1,1,1,1)

charizard.take_damage(50)
charizard.take_damage(50)


charizard.talk()
bulbasaur.talk()
testmon.talk()


your_pokemon = charizard
enemy_pokemon = bulbasaur



# while True:
#     # attack_opt = input(f"hva vil du angripe med?\n 1 {flamethrower}")
#     # enemy_attack_opt = enemy_move_calc_func
#     # if your_pokemon.speed > enemy_pokemon.speed:
#     #     print(f"{your_pokemon.name} går først")
#     # else:
#     #     print(f"{enemy_pokemon.name} går først")
