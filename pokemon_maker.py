import requests

from pokemon_class import Pokemon
from move_class import Move


POKEAPI_URL = "https://pokeapi.co/api/v2"


def get_api_data(endpoint):
    response = requests.get(
        f"{POKEAPI_URL}/{endpoint}",
        timeout = 10
    )

    response.raise_for_status()
    return response.json()


def get_stat(stats, stat_name):
    for stat in stats:
        if stat["stat"]["name"] == stat_name:
            return stat["base_stat"]

    raise ValueError(f"Fant ikke stat '{stat_name}'")

def get_moves_available_for_lvl(data, level):
    """ 
    Denne funksjonen returnerer alle moves som en pokemon kan lære, sortert i kategorier \n
    kategoriene er moves som læres fra level-up og moves som læres med en machine (TMs/HMs)
    """
    moves_from_machine = set()
    moves_from_level_up = set()
    
    for move_entry in data["moves"]:
        move_name = move_entry["move"]["name"]
        
        for details in move_entry["version_group_details"]:
            
            if details["level_learned_at"] <= level:
                method = details["move_learn_method"]["name"]
                
                if method == "level-up":
                    moves_from_level_up.add(move_name)
                elif method == "machine":
                    moves_from_machine.add(move_name)
                    
    return list(moves_from_level_up), list(moves_from_machine)
                

def get_pokemon_move_names(data, limit=4):
    """
    Henter navnene på de første move-ene Pokémonen kan lære.
    Dette er bare en enkel løsning foreløpig.
    """
    move_names = []

    for move_data in data["moves"]:
        move_name = move_data["move"]["name"]
        move_names.append(move_name)

        if len(move_names) >= limit:
            break

    return move_names


def make_move(move_name: str) -> object:
    """
    Henter ett move fra PokéAPI og lager et Move-objekt.
    """
    data = get_api_data(f"move/{move_name}")

    return Move(
        name = data["name"],
        element = data["type"]["name"],
        power = data["power"] or 0,
        dmg_category = data["damage_class"]["name"],
        accuracy = data["accuracy"] or None,
        priority = data["priority"]
    )


def make_pokemon(pokemon_name: str, move_names: list = None, level: int = 100) -> object:
    """
    Henter en Pokémon fra PokéAPI og lager et nytt Pokemon-objekt.
    Hvis moves ikke er spesifisert vil moves bli hentet fra pokeAPI
    """
    
    pokemon_name = pokemon_name.strip().lower()
    
    data = get_api_data(f"pokemon/{pokemon_name.lower()}")
    species_data = get_api_data(f"pokemon-species/{pokemon_name.lower()}")
    

    stats = data["stats"]
    
    element_1 = data["types"][0]["type"]["name"]
    if len(data["types"]) > 1:
        element_2 = data["types"][1]["type"]["name"]
    else:
        element_2 = "None"

    name = data["name"]
    hp = get_stat(stats, "hp")
    attack = get_stat(stats, "attack")
    defence = get_stat(stats, "defense")
    sp_attack = get_stat(stats, "special-attack")
    sp_defence = get_stat(stats, "special-defense")
    speed = get_stat(stats, "speed")
    base_exp = data["base_experience"]
    catch_rate = species_data["capture_rate"]

    if move_names is None:
        move_names = get_pokemon_move_names(data, limit=4)

    moves = []

    for move_name in move_names:
        move = make_move(move_name)
        moves.append(move)
    
    if level > 100:
        level = 100
    if level < 1:
        level = 1

    return Pokemon(
        name = name,
        element_1 = element_1,
        element_2 = element_2,
        hp = hp,
        defence = defence,
        attack = attack,
        sp_attack = sp_attack,
        sp_defence = sp_defence,
        speed = speed,
        base_exp = base_exp,
        catch_rate = catch_rate,
        moves = moves,
        level = level,
    )
    
    
def does_pokemon_exist(pokemon_name: str):
    """
    Sjekker om Pokémon-navnet finnes i PokéAPI.

    True  hvis Pokémonen finnes \n
    False hvis Pokémonen ikke finnes
    """

    pokemon_name = pokemon_name.strip().lower()
    endpoint = f"pokemon/{pokemon_name}"

    try:
        get_api_data(endpoint)
        return True

    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            return False

        print("Det oppstod en feil.")
        print(error)
        return False
    