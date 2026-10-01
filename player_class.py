class Player():
    def __init__(self, name: str):
        self.name = name
        
        self.team = []
        self.pc = []
    
    def add_pokemon(self, pokemon: object) -> str:
        if len(self.team) < 6:
            self.team.append(pokemon)
            return f"{pokemon.name} er nå i laget ditt"
        else:
            self.pc.append(pokemon)
            return f"{pokemon.name} ble sendt til din pc"
    
            
        
        