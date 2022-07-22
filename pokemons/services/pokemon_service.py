import requests
from consts import *

pokemon_types = requests.get("https://pokeapi.co/api/v2/type/")
pokemon_types = pokemon_types.json()
pokemon_types = [type["name"] for type in pokemon_types["results"]]


def type_check(type_name: str):
    if type_name not in pokemon_types:  # eventually POKEMON_TYPES if we know it is constant list of types
        raise KeyError(f'Pokemon type "{type_name}" is not specified')


def types_check(type_names: list[str]) -> KeyError:
    for name in type_names:
        type_check(name)
