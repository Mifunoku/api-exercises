# In my solution I prioritize '/' over '\' according to convention going from left to right, so '/|\' would be '//\'
# def domino_effect(iterations: int, combination: str) -> str:
#     """///||\\\|\\|//"""
#     new_combination = ""
#     combination_with_dots = "." + ".".join(list(combination)) + "."
#     print(combination_with_dots)

import time
import datetime
import re

z = r"\\"
y = ".|.\."
rep = {"./.|.": "././.", ".|.\.": ".\.\."}

# use these three lines to do the replacement
rep = dict((re.escape(k), v) for k, v in rep.items())
pattern = re.compile("|".join(rep.keys()))
# text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)


def domino_effect(iterations: int, combination: str):
    """///||\\\|\\|//"""
    combination_with_dots = "." + ".".join(list(combination)) + "."
    replacements = {"/.|.\.": "/.|.\.", "/.|.": "/./.", "|.\.": "\.\."}
    replacements = dict((re.escape(k), v) for k, v in replacements.items())
    pattern = re.compile("|".join(replacements.keys()))
    for _ in range(iterations):
        combination_with_dots = pattern.sub(lambda m: replacements[re.escape(m.group(0))], combination_with_dots)
    combination = combination_with_dots.replace(".", "")

    return combination


def domino_effect_no_dots(iterations: int, combination: str):
    replacements = {"/|\\": "/|\\", "/|": "//", "|\\": "\\\\"}
    replacements = dict((re.escape(k), v) for k, v in replacements.items())
    pattern = re.compile("|".join(replacements.keys()))
    for _ in range(iterations):
        combination = pattern.sub(lambda m: replacements[re.escape(m.group(0))], combination)

    return combination


def domino_effect_recursive(iterations: int, combination: str):
    replacements = {"/|\\": "/|\\", "/|": "//", "|\\": "\\\\"}
    replacements = dict((re.escape(k), v) for k, v in replacements.items())
    pattern = re.compile("|".join(replacements.keys()))
    if iterations > 0:
        old_text = pattern.sub(lambda m: replacements[re.escape(m.group(0))], combination)
        text = domino_effect_recursive(iterations - 1, old_text)
    else:
        text = combination
    return text


# def domino_brute_force(iterations: int, combination: str):
#     standing_dominoes = combination.find_all('|')
#     if combination[position:position+1] ==


if __name__ == "__main__":
    print("domino_effect: \n", r"///|||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect(1, r"///|||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("domino_effect_no_dots: \n", r"///|||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect_no_dots(1, r"///|||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("recursive: \n", r"///|||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect_recursive(1, r"///|||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("domino_effect: \n", r"///|||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect(30, r"///|||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("domino_effect_no_dots: \n", r"///|||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect_no_dots(30, r"///|||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("recursive: \n", r"///|||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect_recursive(30, r"///|||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("domino_effect: \n", r"///||||||||||||||||||||||||||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect(10, r"///||||||||||||||||||||||||||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("domino_effect_no_dots: \n", r"///||||||||||||||||||||||||||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect_no_dots(10, r"///||||||||||||||||||||||||||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")

    print("recursive: \n", r"///||||||||||||||||||||||||||||\\\||\\|//")
    start_time = time.perf_counter_ns()
    print(domino_effect_recursive(10, r"///||||||||||||||||||||||||||||\\\||\\|//"))
    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")
