"""Practice for the final."""


def odd_and_even(nums: list[int]) -> list[int]:
    """Returns a new list containing odd at even index."""
    oddeven: list[int] = []
    i: int = 1
    for item in nums:
        if ((item % 2 != 0) and (i % 2 == 0)):
            oddeven.append(item)
        i += 1
    return oddeven


def vowels_and_threes(word: str) -> str:
    """Returns new string containing char at index mult 3 or vowel."""
    vowthree: str = ""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    i: int = 0
    i2: int = 0
    while (i < len(word)):
        if (i % 3 == 0):
            vowthree += word[i]
        else:
            while (i2 < len(word)):
                if word[i] == vowels[i2]:
                    vowthree += word[i]
                i2 += 1
    return vowthree


def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    averages: dict[str, float] = {}
    i: int = 0
    sum: float = 0
    for item in grades:
        while (i < len(item)):
            sum += float(item[i])
            i += 1
        sum = sum / len(item)
        averages[item] = sum
        sum = 0
    return averages
