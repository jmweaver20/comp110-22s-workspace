"""Worldle Game using functions."""

__author__ = "730397253"


def contains_char(guess: str, single_char: str) -> bool:
    """Searches for a single character in the 'guess' string."""
    assert len(single_char) == 1
    i: int = 0

    while (i < len(guess)):
        if (i == (len(guess) - 1) and guess[i] != single_char):
            return False
        if(guess[i] == single_char):
            return True
        i = i + 1
    return False 


def emojified(guess: str, secret: str) -> str:
    """Return string of emoji which codifies the string input."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_string: str = ""
    i: int = 0

    while (i < len(secret)):
        if (guess[i] == secret[i]):
            emoji_string += GREEN_BOX
            i += 1
        elif (contains_char(secret, guess[i])):
            emoji_string += YELLOW_BOX
            i += 1
        else:
            emoji_string += WHITE_BOX
            i += 1
    return emoji_string 


def input_guess(expected_length: int) -> str:
    """Checks to make sure the guess is the expected length. Allows re-guesses."""
    length = str(expected_length)
    word = str(input("Enter a " + length + " character word: "))

    if (len(word) == expected_length):
        return word
    else:
        while (len(word) < expected_length or len(word) > expected_length):
            word = str(input("That wasn't " + length + " chars! Try again: "))
    return word
