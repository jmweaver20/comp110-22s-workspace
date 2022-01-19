"""EX01 - Chardle - A cute step toward Worldle."""

_author_ = "730397253"

"""THIS NEEDS TO CHECK FOR LESS THAN 5 CHARACTERS TOO"""
five_char_word = str(input("Enter a 5-character word: "))
if (len(five_char_word) > 5):
    print("Error: Word must contain 5 characters")
    exit()

if (len(five_char_word) < 5):
    print("Error: Word must contain 5 characters")
    exit()

single_char = str(input("Enter a single character: "))
if (len(single_char) > 1):
    print("Error: Character must be a single character.")
    exit()

match_count = int(0)
print("Searching for " + single_char + " in " + five_char_word)

if (single_char == five_char_word[0]):
    print(single_char + " found at index 0")
    match_count = match_count + 1
if (single_char == five_char_word[1]):
    print(single_char + " found at index 1")
    match_count = match_count + 1
if (single_char == five_char_word[2]):
    print(single_char + " found at index 2")
    match_count = match_count + 1
if (single_char == five_char_word[3]):
    print(single_char + " found at index 3")
    matchcount = match_count + 1
if (single_char == five_char_word[4]):
    print(single_char + " found at index 4")
    match_count = match_count + 1

if (match_count >= 1):
    print(str(match_count) + " instances of " + single_char + " found in " + five_char_word)
else:
    print("No instances of " + single_char + " found in " + five_char_word)
