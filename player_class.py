from pokeball_class import pokeball, greatball, ultraball
from pokemon_class import Pokemon

class Player():
    def __init__(self, name: str):
        self.name = name
        
        self.team = []
        self.pc = []
        
        self.pokeballs = {
            "pokeball": {
                "pokeball_type": pokeball, 
                "amount": 0
                },
            "greatball": {
                "pokeball_type": greatball, 
                "amount": 0
                },
            "ultraball": {
                "pokeball_type": ultraball,
                "amount": 1
                },
        }
    
    def has_pokeballs(self) -> bool:
        for i in range(len(self.pokeballs)):
            if self.pokeballs[i]["amount"] > 0:
                return True
        else:
            return False
        
    def add_pokemon(self, pokemon: object) -> str:
        if len(self.team) < 6:
            self.team.append(pokemon)
            return f"{pokemon.name} er nå på laget ditt"
        else:
            self.pc.append(pokemon)
            return f"{pokemon.name} ble sendt til din pc"
        
    def get_remaining_pokemon(self, current_pokemon: Pokemon) -> list[object]:
        remaining_pokemon = []
        for pokemon in self.team:
            if pokemon.is_fainted() == False and pokemon != current_pokemon:
                remaining_pokemon.append(pokemon)
        return remaining_pokemon
    
    def add_pokeballs(self, pokeball_type: str, amount: int):
        if pokeball_type in self.pokeballs:
            self.pokeballs[pokeball_type]["amount"] += amount
    
    def remove_pokeballs(self, pokeball_type: str, amount: int = 1):
        if pokeball_type in self.pokeballs:
            if self.pokeballs[pokeball_type]["amount"] >= amount:
                self.pokeballs[pokeball_type]["amount"] -= amount
            else:
                self.pokeballs[pokeball_type]["amount"] = 0
    
    def use_pokeball(self, pokeball_type: str):
        if self.pokeballs[pokeball_type]["ammount"] >= 0:
            self.pokeballs[pokeball_type]["ammount"] -= 1
    
    def get_available_pokeballs(self) -> list[object]:
        pokeball_list = []
        for ball, info in self.pokeballs.items():
            if info["amount"] > 0:
                pokeball_list.append((info["pokeball_type"], info["amount"]))
        return pokeball_list