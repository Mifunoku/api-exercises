import __future__

import requests
from consts import *
from pokemon_service import type_check, types_check

# I assume that attacker type is only one
def attack_multiplier(attacker_type: str, defender_type: str) -> str:
    multiplier = 1
    defender_types = defender_type.split()
    try:
        type_check(attacker_type)
        types_check(defender_types)
    except KeyError as e:
        return e.args
    type_content = requests.get(f"https://pokeapi.co/api/v2/type/{attacker_type}").json()
    damage_relations = type_content["damage_relations"]
    atk_dict = dict()
    for item in damage_relations["double_damage_to"]:
        atk_dict[item["name"]] = 2
    for item in damage_relations["half_damage_to"]:
        atk_dict[item["name"]] = 0.5
    for item in damage_relations["no_damage_to"]:
        atk_dict[item["name"]] = 0
    for name in defender_types:
        if atk_dict.get(name) != None:
            multiplier *= atk_dict.get(name)

    return f"{multiplier}x"


if __name__ == "__main__":
    attack_multiplier("fire", "ice")
