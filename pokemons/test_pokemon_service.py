import pytest
from pokemon_service import type_check, types_check
from attack_multiplier import attack_multiplier


def test_correct_single_type_check():
    name = "fire"
    assert type_check(name) == None


def test_correct_double_type_check():
    name = "fire ice"
    names = name.split()
    assert types_check(names) == None


def test_incorrect_single_type_check():
    name = "moulder"
    with pytest.raises(Exception) as exc_info:
        type_check(name)
    assert exc_info.value.args[0] == f'Pokemon of type "{name}" is not specified'


def test_incorrect_double_type_check():
    name = "moulder grounder"
    names = name.split()
    with pytest.raises(Exception) as exc_info:
        types_check(names)
    assert exc_info.value.args[0] == f'Pokemon of type "{names[0]}" is not specified'


def test_incorrect_double_type_check_first_correct():
    name = "fire grounder"
    names = name.split()
    with pytest.raises(Exception) as exc_info:
        types_check(names)
    assert exc_info.value.args[0] == f'Pokemon of type "{names[1]}" is not specified'


def test_attack_multiplier():
    assert attack_multiplier("fire", "grass") == "2x"
    assert attack_multiplier("fighting", "ice rock") == "4x"
    assert attack_multiplier("psychic", "poison dark") == "0x"
    assert attack_multiplier("water", "normal") == "1x"
    assert attack_multiplier("fire", "rock") == "0.5x"
    assert attack_multiplier("moulder", "rock") == ('Pokemon of type "moulder" is not specified',)
