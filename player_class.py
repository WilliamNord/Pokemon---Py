from pokeball_class import pokeball, greatball, ultraball

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
    
    def add_pokemon(self, pokemon: object):
        if len(self.team) < 6:
            self.team.append(pokemon)
            return f"{pokemon.name} er nå i laget ditt"
        else:
            self.pc.append(pokemon)
            return f"{pokemon.name} ble sendt til din pc"
    
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
        for ball, data in self.pokeballs.items():
            if data["amount"] > 0:
                info = ball, data["amount"]
                pkbl_list.append(info)
        return pkbl_list
                
            
        
        