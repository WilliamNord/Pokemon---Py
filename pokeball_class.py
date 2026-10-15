class Pokeball:
    def __init__(self, pkbl_type: str):
        self.pkbl_type = pkbl_type.lower()
        
    def get_ballmod(self):
        """ 
        Denne funksjonen returnerer catchrate modifyer som 1, 1.5 eller 2.
        """
        match self.pkbl_type:
            case "pokeball":
                return 1.0
            case "greatball":
                return 1.5
            case "ultraball":
                return 2.0
            case _:
                return 1.0

pokeball = Pokeball("pokeball")
greatball = Pokeball("greatball")
ultraball = Pokeball("ultraball")