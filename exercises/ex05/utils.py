"""Practice with functions and testing."""

__author__ = "730397253"


def only_evens(nums: list[int]) -> list[int]:
    """Goes through a list and returns only the even numbers."""
    evens: list[int] = list()
    for item in nums:
        if (item % 2 == 0):
            evens.append(item)
    return evens


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Returns a list subset of values between start and end (not inclusive) indices."""
    subset: list[int] = list()

    if (len(nums) == 0 or start > len(nums) or end <= 0):
        return subset
    if (start < 0):
        start = 0
    if (end > len(nums) - 1):
        end = len(nums) - 1
    
    i: int = start
    while (i < end):
        subset.append(nums[i])
        i += 1
    return subset


def concat(nums1: list[int], nums2: list[int]) -> list[int]:
    """Given two lists returns a list which has all items in it."""
    full_list: list[int] = list()

    for item in nums1:
        full_list.append(item)
    for item in nums2:
        full_list.append(item)
    
    return full_list