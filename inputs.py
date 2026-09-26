from pokemon_maker import does_pokemon_exist


def ask_for_pokemon(prompt: str) -> str:
    """ 
    spør brukeren om et pokemon navn og sjekker om den pokemonen finnes
    
    Hvis pokemonen finnes i api-et til pokeAPI så returnerer den navnet til pokemonen
    Hvis pokemonen ikke finnes, blir brukeren spurt igjen helt til en pokemon blir funnet.
    """
    while True:
        pokemon_name = input(prompt).strip().lower()

        if does_pokemon_exist(pokemon_name):
            return pokemon_name

        print(f"Fant ikke Pokémonen '{pokemon_name}'.")
        print("Prøv igjen.")