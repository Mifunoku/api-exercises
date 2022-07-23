import pytest

from domino_effect import domino_effect, domino_effect_reversed


def test_falling():
    assert domino_effect(1, r"||//||\||/\|") == r"||///\\||/\|"
    assert domino_effect(2, r"||//||||\||/\|") == r"||////\\\||/\|"
    assert domino_effect(1, r"|\|//||\||/\|") == r"\\|///\\||/\|"
    assert domino_effect(1, r"|\|//||\||/\/|\\") == r"\\|///\\||/\/|\\"
    assert domino_effect(0, r"||//||\||/\|") == r"||//||\||/\|"


def test_reversing():
    assert domino_effect_reversed(2, r"||////\\\|////|") == r"||//||||\|//|||"
    assert domino_effect_reversed(2, r"\\////\\\|////|//") == r"||//||||\|//|||||"
    assert domino_effect_reversed(2, r"|//\\\///|/\\") == r"|||||\/||||||"
    assert domino_effect_reversed(2, r"\||/\\\\/|\\") == r"||||||\\||||"
    assert domino_effect_reversed(2, r"\||/\\\\/|\\/") == r"||||||\\|||||"
    assert domino_effect_reversed(-2, r"\||/\\\\/|\\") == r"\||/\\\\/|\\"
    assert domino_effect_reversed(0, r"\||/\\\\/|\\") == r"\||/\\\\/|\\"


def test_falling_exception():
    with pytest.raises(Exception) as exc_info:
        domino_effect(1, r"|mn|//||\||/\|")
    assert exc_info.value.args[0] == r"Combination can only contains \ / |"

    with pytest.raises(Exception) as exc_info:
        domino_effect(1, r"")
    assert exc_info.value.args[0] == r"Combination can't be empty"


def test_reversing_exception():
    with pytest.raises(Exception) as exc_info:
        domino_effect_reversed(1, r"|mn|//||\||/\|")
    assert exc_info.value.args[0] == r"Combination can only contains \ / |"

    with pytest.raises(Exception) as exc_info:
        domino_effect_reversed(1, r"")
    assert exc_info.value.args[0] == r"Combination can't be empty"
