#metode for super effektive typer
all_elements = {
    "normal": {
        "strong": [],
        "weak": ["rock", "steel"],
        "no_effect": ["ghost"],
    },
    "fire": {
        "strong": ["grass", "ice", "bug", "steel"],
        "weak": ["ground", "water", "rock",],
        "no_effect": []
        },
    "water": {
        "strong": ["fire", "ground"],
        "weak": ["grass", "electric"],
        "no_effect": [],
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
        "weak": ["fire", "flying", "poison", "fighting", "ghost", "steel", "fairy"],
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
        "weak": ["fire", "poison", "steel"],
        "no_effect": [],
    },
    
}

def check_effectiveness(pk_defender: object, attacking_move: object, elements_nb: int) -> int:
    """ 
    Denne funksjonen tar inn én pokemon og ett moves. 
    Hvis defender sitt element blir funnet i ordboken for elemnter, er attacking_move enten:
    super effektiv, ikke effektiv, har null effekt eller er nøytralt.
    disse resultatene peker på henholdsvis koefisientene 2, 0.5, 0 og 1 
    """
    pk_element = pk_defender.elements[elements_nb]
    
    if pk_element in all_elements[attacking_move.element]["strong"]:
        return 2
    elif pk_element in all_elements[attacking_move.element]["weak"]:
        return 0.5
    elif pk_element in all_elements[attacking_move.element]["no_effect"]:
        return 0
    else:
        return 1
    
def total_effectiveness(defender: object, attacking_move: object):
    return check_effectiveness(defender, attacking_move, 0) * check_effectiveness(defender, attacking_move, 1)
        

def show_effectiveness(element: str):
    liste = []
    for i in range(len(all_elements[element]["strong"])):
        liste.append(all_elements[element]['strong'][i])
        
    print(f"{element} er bra mot {liste}")
    
def effectiveness_tekst(sum_effectiveness: int) -> str:

    match sum_effectiveness:
        case 4:
            return f"er MEGA effektivt!"
        case 2:
            return f"er SUPER effektivt!"
        case 1:
            return f""
        case 0.5 | 0.25:
            return f"er ikke veldig effektivt"
        case 0:
            return f"hadde INGEN effekt!"

print(effectiveness_tekst(0.25))
# def effectiveness_tekst(defender: object, move: object) -> str:
#     effectiveness = [check_effectiveness(defender, move, 0), check_effectiveness(defender, move, 1)]
    
#     sum_effectiveness = effectiveness[0] * effectiveness [1]
    
#     match sum_effectiveness:
#         case 4:
#             return f"{move} er MEGA effektivt!"
#         case 2:
#             return f"{move} er SUPER effektivt!"
#         case 0:
#             return f"{move} hadde INGEN effekt!"
#         case 1:
#             return ""