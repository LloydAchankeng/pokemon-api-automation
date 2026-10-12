from logger import setup_logger
from pokemon_api import get_pokemon, get_stats, get_abilities, get_moves

def main():
    setup_logger()

    pokemon_name = input("Enter a Pokémon name: ")

    data = get_pokemon(pokemon_name)

    if not data:
        print("Could not fetch Pokémon data.")
        return

    print("\n=== Pokémon Data ===")
    print(f"Name: {data['name'].title()}")
    print(f"ID: {data['id']}")

    print("\nStats:")
    stats = get_stats(data)
    for stat, value in stats.items():
        print(f"- {stat}: {value}")

    print("\nAbilities:")
    abilities = get_abilities(data)
    for ability in abilities:
        print(f"- {ability}")

    print("\nMoves:")
    moves = get_moves(data)
    for move in moves[:10]:  # only show first 10 moves
        print(f"- {move}")

if __name__ == "__main__":
    main()
