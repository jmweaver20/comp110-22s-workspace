"""Wordle program using loops & implementing more advanced character methods"""

__author__ = "730397253"

secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0  # Index Tracker
emoji_guess: str = ""

while (len(user_guess) < len(secret_word) or len(user_guess) > len(secret_word)):
    user_guess = str(input("That was not 6 letters! Try again: "))

while (i < len(secret_word)):
    if (secret_word[i] == user_guess[i]):
        emoji_guess = emoji_guess + GREEN_BOX
    else:
        emoji_guess = emoji_guess + WHITE_BOX
    i = i + 1

print(emoji_guess)

if (user_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite! Play again soon.")