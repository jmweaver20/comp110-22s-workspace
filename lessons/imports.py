"""Examples of importing in python."""


# Allows us to use helpers as hp instead of writing
# out of all helpers
from lessons import helpers as hp


def main() -> None:
    """Entrypoint of our program."""
    print(hp.powerful(2, 4))


if __name__ == "__main__":
    main()