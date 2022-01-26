"""Wordle program using loops & implementing more advanced character methods"""

__author__ = "730397253"

# This chunk defines the secret word and allows user
# to input a guess.
secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")

# These lines provide the code for the box
# diagrams seen as output. 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0  # Index Tracker for Main Loop
i2: int = 0  # Index Tracker for Yellow Boxes - make sure we need this?
char_exist: bool = False
emoji_guess: str = ""

# This loop ensures that the user's guess word is matching in length
# to the secret word.
while (len(user_guess) < len(secret_word) or len(user_guess) > len(secret_word)):
    user_guess = str(input("That was not 6 letters! Try again: "))

# These loops and statement provide the checking mechanism for 
# the individual characters in the user's guess and the secret word.
while (i < len(secret_word)):

    if (secret_word[i] == user_guess[i]):
        emoji_guess = emoji_guess + GREEN_BOX
        i = i + 1
    else:
        i2 = 0
        char_exist = False
        while ((char_exist is not True) and i2 < len(secret_word)):
            if (secret_word[i2] == user_guess[i]):
                char_exist = True
            else:
                i2 = i2 + 1
        if (char_exist):
            emoji_guess = emoji_guess + YELLOW_BOX
        else:
            emoji_guess = emoji_guess + WHITE_BOX
        i = i + 1

# This prints the blocks of color corresponding
# to the user's guess (yellow, green, and white)
print(emoji_guess)

if (user_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

# Instructions said to use f-string outputs but I haven't found a place to use those?
# why does the char_exist != True logic not working (it's underlined)
# white box when char_exist is false isn't printing?