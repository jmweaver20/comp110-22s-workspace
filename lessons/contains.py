"""Example of writing a function to search a list."""

# Define a function named contains
# Parameters:
#   1. needle - the str we're searching for
#   2. haystack - the list of str values we're searching through

# Alg: for each item in haystack:
#   Test if equal to needle we're looking for
#   if yes return true
#   else keep going and if not found return false


def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answer: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answer):
        print("We're letting you in the secret club!")
    else:
        print("Go back to Davis")


def contains(needle: str, haystack: list[str]) -> bool:
    "Finds needle in haystack"
    for item in haystack:
        if (item == needle):
            return True
    return False


print(__name__)
if __name__ == "__main__":
    main()