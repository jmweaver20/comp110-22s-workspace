"""EX06 - Using Dictionaries and Functions to find maxes, invert key-values, and count occurences."""

__author__ = "730397253"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts the key and value pairs."""
    inverted: dict[str, str] = dict()
    for key in a:
        if (a[key] in inverted):
            raise KeyError("Cannot have duplicate keys!")
        else:
            inverted[a[key]] = key
    return inverted


def favorite_color(a: dict[str, str]) -> str:
    """Give dictionary of names and favorite colors, returns most listed color."""
    colors: str = ""
    input_dict = a
    color_count: dict[str, int] = dict()
    
    for key in input_dict:
        if input_dict[key] in color_count:
            color_count[input_dict[key]] += 1
        else:
            color_count[input_dict[key]] = 1

    max_val: int = 0
    for key in color_count:
        if color_count[key] > max_val:
            max_val = color_count[key]
            colors = key
    return colors


def count(a: list[str]) -> dict[str, int]:
    """Returns a dictionary where each key is a value in the list and the key value is the number of times it occurs."""
    repeats: dict[str, int] = dict()
    i: int = 0
    while (i < len(a)):
        if a[i] in repeats:
            repeats[a[i]] += 1
        else:
            repeats[a[i]] = 1
        i += 1
    return repeats