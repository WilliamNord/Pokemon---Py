from pokeball_class import pokeball, greatball, ultraball
from pokemon_class import Pokemon

class Player():
    def __init__(self, name: str):
        self.name = name
        
        self.team = []
        self.pc = []
        
        self.pokeballs = {
            "pokeball": {
                "pkbl_type": pokeball, 
                "amount": 0
                },
            "greatball": {
                "pkbl_type": greatball, 
                "amount": 0
                },
            "ultraball": {
                "pkbl_type": ultraball, 
                "amount": 0
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
            return f"{pokemon.name} er nå i laget ditt"
        else:
            self.pc.append(pokemon)
            return f"{pokemon.name} ble sendt til din pc"
        
    def get_remaining_pokemon(self, current_pokemon: Pokemon) -> list[object]:
        remaining_pokemon = []
        for pokemon in self.team:
            if pokemon.is_fainted() == False and pokemon != current_pokemon:
                remaining_pokemon.append(pokemon)
        return remaining_pokemon
    
    def add_pokeballs(self, pkbl_type: str, amount: int):
        if pkbl_type in self.pokeballs:
            self.pokeballs[pkbl_type]["amount"] += amount
    
    def remove_pokeballs(self, pkbl_type: str, amount: int = 1):
        if pkbl_type in self.pokeballs:
            if self.pokeballs[pkbl_type]["amount"] >= amount:
                self.pokeballs[pkbl_type]["amount"] -= amount
            else:
                self.pokeballs[pkbl_type]["amount"] = 0
    
    def get_available_pkbls(self):
        pkbl_list = []
        for ball, info in self.pokeballs.items():
            if info["amount"] > 0:
                pkbl_list.append(ball)
        return pkbl_list