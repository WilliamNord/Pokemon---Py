import requests

pokemon = input("hvilken pokemon: ")

# Hent data fra PokeAPI
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
data = response.json()

pokemon_stats = {}

# Gå igjennom listen med stats
for item in data["stats"]:
    stat_name = item["stat"]["name"]
    base_value = item["base_stat"]  
    pokemon_stats[stat_name] = base_value


print(f"dette er {pokemon} sine stats")
for name, value in pokemon_stats.items():
    print(f"{name}: {value}")

