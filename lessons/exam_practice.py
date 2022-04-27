"""Final Exam Review Questions & Answers."""


def reverse_multiply(mult: list[int]) -> list[int]:
    """Returns list of ints in reverse order and doubled."""
    revmult: list[int] = []
    i: int = (len(mult) - 1)

    while (i >= 0):
        revmult.append(mult[i] * 2)
        i -= 1

    return revmult


test: list[int] = [1, 2, 3]
print("Testing Reverse Multiply: [1, 2, 3]")
print(reverse_multiply(test))


def free_biscuits(games: dict[str, list[int]]) -> dict[str, bool]:
    """Returns new dict maps each game to bool if above 100+"""
    biscuit: dict[str, bool] = {}
    sum: int = 0
    for item in games:
        for val in games[item]:
            sum += val
        if sum >= 100:
            biscuit[item] = True
        else:
            biscuit[item] = False
    return biscuit


def multiples(nums: list[int]) -> list[bool]:
    """Returns a list of bools for multiples preceding val."""
    mults: list[bool] = []
    i: int = 0
    while (i < len(nums)):
        if i == 0:
            if nums[0] % nums[len(nums) - 1] == 0:
                mults.append(True)
                i += 1
            else:
                mults.append(False)
                i += 1
        else:
            if nums[i] % nums[i - 1] == 0:
                mults.append(True)
                i += 1
            else:
                mults.append(False)
                i += 1
    return mults


print("Testing for multiples function.")
print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))


def merge_lists(l1: list[str], l2: list[int]) -> dict[str, int]:
    """Merges two lists"""
    merged: dict[str, int] = {}
    if len(l1) != len(l2):
        return merged
    i: int = 0
    for item in l1:
        merged[item] = l2[i]
        i += 1
    return merged


print("Testing for merge")
l1: list[str] = ["happy", "sad", "red"]
l2: list[int] = [1, 2, 3]
print(merge_lists(l1, l2))