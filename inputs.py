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

def ask_player_choice(options: list):
    """ 
    Denne funnksjonen spør spilleren hvor de vil gå. for eksempel "gresset" eller "pokecenter".
    alle stedene har sine egne funksjoner og lar spilleren gjøre ulike ting.
    Denne funksjonen lar spilleren enten skrive inn indexen eller navnet på hvor de vil gå.
    F.eks: 1 og "grass" går til samme sted
    """
    for x, name in enumerate(options):
        print((x + 1), name)
    
    while True:
        choice = input("hvor vil du gå?: ").lower().strip()
        
        if choice.isdigit():
            index = int(choice)
            
            if 1 <= index <= len(options):
                return options[index - 1]
            else:
                print(f"ugyldig nummer, du må skrivet ett tall mellom 1 og {len(options)}")
                continue
        
        options_lower = [opt.lower() for opt in options]
        
        if choice in options_lower:
            return options[options.index(choice)]
        
        print("ugyldig index eller navn, prøv igjen")

# def ask_player_route(route_options):
#     for index, name in enumerate(route_options):
#         print(index+1, name)
    
#     while True:
#         choice = 