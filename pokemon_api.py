import requests
import logging

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name):
    try:
        response = requests.get(BASE_URL + name.lower())
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched data for {name}")
        return data

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Connection error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    return None


def get_stats(data):
    if not data:
        return None
    return {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}


def get_abilities(data):
    if not data:
        return None
    return [ability["ability"]["name"] for ability in data["abilities"]]


def get_moves(data):
    if not data:
        return None
    return [move["move"]["name"] for move in data["moves"]]
