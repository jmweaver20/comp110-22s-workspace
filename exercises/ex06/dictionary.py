"""DONT FORGET TO ADD THIS"""

__author__ = "730397253"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts the key and value pairs."""
    inverted = dict[str, str]
    inverted = dict()
    for key in a:
        # is this valid code?
        if (a[key] == inverted[a[key]]):
            raise KeyError("Cannot have duplicated keys!")
        else:
            inverted[a[key]] = key
    return inverted


def favorite_color(a: dict[str, str]) -> str:
    """Give dictionary of names and favorite colors, returns most listed color."""
    colors: str = ""
    color_count = dict[str, int]
    color_count = dict()

    # Fills color count dictionary with colors and how many times they repeat.
    for key in a:
        color_count[a[key]] += 1

    # Fills the occurence list with just the numerical values.
    occurences: list[int] = list()
    for key in color_count:
        occurences.append(color_count[key])
    
    # Goes through the list of values and finds the largest one.
    max_val: int = 0
    i: int = 0
    while(i < len(occurences)):
        if (occurences[i] > max_val):
            max_val = occurences[i]
        i += 1

    # Goes through the color count dictionary and finds the corresponding max value color occurence
    for key in color_count:
        if (color_count[key] == max_val):
            colors = color_count[key]

    return colors
