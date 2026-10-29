from pokemon_maker import does_pokemon_exist
from pokemon_class import Pokemon
from move_class import Move
import time

sleep_value = 1.5

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
        
test = 12
def ask_player_move(your_pokemon: Pokemon) -> Move:
    """ 
    denne funksjonen spør spilleren om hvilken av alle moves til dere pokemon som de vil bruke
    """
    while True:
        print("\n")
        for i, move in enumerate(your_pokemon.moves):
            print(f"{i + 1}. {move.name:<{test}} TYPE: {move.element} BP: {move.power}, ACCURACY: {move.accuracy}")

        try:
            player_choice = int(input("hvilket move vil du bruke?: "))

            if 1 <= player_choice <= len(your_pokemon.moves):
                return your_pokemon.moves[player_choice - 1]
            else:
                print("ERROR: du må velge et move du har")
                time.sleep(sleep_value)

        except ValueError:
            print("du må skrive et tall")
            time.sleep(sleep_value)

go_back_return = "[go back]"

#burde legge til at tomme inputs ignoreres
def ask_player_choice(options: list, can_go_back: bool = False, prompt: str = "hva vil du gjøre?: ", ) -> str:
    """ 
    Denne funnksjonen spør spilleren hvor de vil gå. for eksempel "gresset" eller "pokecenter".
    alle stedene har sine egne funksjoner og lar spilleren gjøre ulike ting.
    Denne funksjonen lar spilleren enten skrive inn indexen eller navnet på hvor de vil gå.
    F.eks: 1 og "grass" går til samme sted
    """
    print()
    if can_go_back == True:
        options.append(go_back_return)
    for x, name in enumerate(options):
        print((x + 1), name)
    
    options_lower = [opt.lower() for opt in options]
    
    while True:
        choice = input(prompt).lower().strip()
        
        if choice.isdigit():
            index = int(choice)
            
            if 1 <= index <= len(options):
                return options[index - 1]
            else:
                print(f"ugyldig nummer, du må skrivet ett tall mellom 1 og {len(options)}")
                continue
            
            
        if choice in options_lower:
            return options[options.index(choice.lower())]
        
        
        print("ugyldig index eller navn, prøv igjen")
