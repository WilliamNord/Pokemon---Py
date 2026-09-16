#metode for super effektive typer
elementer = {
    "normal": {
        "strong": [],
        "weak": ["rock", "steel"],
        "immune": ["ghost"],
    },
    "fire": {
        "strong": ["grass", "ice", "bug", "steel"],
        "weak": ["ground", "water", "rock",],
        },
    "water": {
        "strong": ["fire", "ground","electric"],
        "weak": ["grass", "electric"],
    },
    "grass": {
        "strong": ["water", "rock", "ground",],
        "weak": ["grass", "fire", "bug", "flying", "poison", "dragon", "steel"],
        "no_effect": [],
    },
    "electric": {
        "strong": ["water", "flying"],
        "weak": ["grass", "electric", "dragon"],
        "no_effect": ["ground"],
    },
    "bug":{ 
        "strong": ["grass", "psychic", "dark"],
        "weak": ["fire", "flying", "poison", "fighting", "ghost", "steek", "fairy"],
        "no_effect": [],
    },
    "flying":{ 
        "strong": ["grass", "bug", "fighting"],
        "weak": ["electric", "rock", "steel"],
        "no_effect": [],
    },
    "rock":{ 
        "strong": ["fire", "bug", "flying", "ice"],
        "weak": ["ground", "fighting", "steel"],
        "no_effect": [],
    },
    "poison":{ 
        "strong": ["grass", "fairy"],
        "weak": ["rock", "poison", "ground", "ghost"],
        "no_effect": ["steel"],
    },
    "ground":{ 
        "strong": ["fire", "electric", "rock", "poison", "steel"],
        "weak": ["grass", "bug"],
        "no_effect": ["flying"],
    },
    "ice":{ 
        "strong": ["grass", "flying", "ground", "dragon"],
        "weak": ["fire", "water", "ice", "steel"],
        "no_effect": [],
    },
    "fighting":{ 
        "strong": ["normal", "rock", "ice", "dark", "steel"],
        "weak": ["bug", "flying", "poison", "psychic", "fairy"],
        "no_effect": ["ghost"],
    },
    "psychic":{ 
        "strong": ["poison", "fighting"],
        "weak": ["psychic", "steel"],
        "no_effect": ["dark"],
    },
    "ghost":{ 
        "strong": ["psychic", "ghost"],
        "weak": ["dark"],
        "no_effect": ["normal"],
    },
    "dragon":{ 
        "strong": ["dragon"],
        "weak": ["steel"],
        "no_effect": ["fairy"],
    },
    "dark":{ 
        "strong": ["psychic", "ghost"],
        "weak": ["fighting", "dark", "fairy"],
        "no_effect": [],
    },
    "steel":{ 
        "strong": ["rock", "ice", "fairy"],
        "weak": ["fire", "water", "electric", "steel"],
        "no_effect": [],
    },
    "fairy":{ 
        "strong": ["fighting", "dragon", "dark"],
        "weak": ["fire", "posion", "steel"],
        "no_effect": [],
    },
    
}

print(elementer["fire"]["strong"][0])

print(f"fire er bra mot {elementer["fire"]["strong"]}")

def show_effectiveness(): 
    for element in elementer:
        print(f"{element} er sterk mot {elementer[element]["strong"]}")
    
        
        