"""Worldle Game using functions."""

__author__ = "730397253"


def contains_char(guess: str, single_char: str) -> bool:
    """Searches for a single character in the 'guess' string."""
    assert len(single_char) == 1
    i: int = 0  # Counter Variable

    while (i < len(guess)):
        if (i == (len(guess) - 1) and guess[i] != single_char):
            return False
        if(guess[i] == single_char):
            return True
        else:
            i = i + 1
