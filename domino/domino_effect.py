import re


def domino_effect(iterations: int, combination: str):
    """
    combination have to be raw string
    In this solution I assumed that combination of '/|\' doesn't change because both of the edge push the middle one
    """
    if re.findall(r"[^\|\/\\]", combination):
        raise KeyError(r"Combination can only contains \ / |")
    if len(combination) == 0:
        raise KeyError("Combination can't be empty")
    if iterations <= 0:
        return combination

    replacements = {"/|\\": "/|\\", "/|": "//", "|\\": "\\\\"}
    replacements = dict((re.escape(k), v) for k, v in replacements.items())
    pattern = re.compile("|".join(replacements.keys()))

    while iterations > 0:
        # optimalization for bigger iterations is commented in lines 18,21,22
        # old_combination = combination
        combination = pattern.sub(lambda m: replacements[re.escape(m.group(0))], combination)
        iterations -= 1
        # if old_combination == combination:
        #     iterations = -1

    return combination


def domino_effect_reversed(iterations: int, combination: str):
    """
    due to python way of interpreting escape characters combination have to be raw string and cant end with single backslash
    """
    if re.findall(r"[^\|\/\\]", combination):
        raise KeyError(r"Combination can only contains \ / |")
    if len(combination) == 0:
        raise KeyError("Combination can't be empty")
    if iterations <= 0:
        return combination

    replacements = {"/\\": "||", "/|\\": "|||", "/|": "||", "|\\": "||"}
    replacements = dict((re.escape(k), v) for k, v in replacements.items())
    pattern = re.compile("|".join(replacements.keys()))

    combination = pattern.sub(lambda m: replacements[re.escape(m.group(0))], combination)
    if combination[0] == "\\":
        combination = "".join(["|", combination[1:]])
    if combination[-1] == "/":
        combination = "".join([combination[:-1], "|"])
    iterations -= 1

    while iterations > 0:
        combination = pattern.sub(lambda m: replacements[re.escape(m.group(0))], combination)
        iterations -= 1

    return combination


if __name__ == "__main__":
    print("One iteration of domino represented in order \n", r"||//||\||/\|:")
    first_fall = domino_effect(1, r"||//||\||/\|")
    print("First fall:")
    print("", first_fall)
    print("Reversed:")
    print("", domino_effect_reversed(1, first_fall))

    print("Two reversed iterations of domino in order \n", r"||////\\\|////|")
    print("", domino_effect_reversed(2, r"||////\\\|////|"))
