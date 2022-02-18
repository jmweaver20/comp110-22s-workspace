"""Testing for the utils.py file"""

__author__ = "730397253"


from exercises.ex05.utils import only_evens, sub
# also need to test oncat


def test_only_evens_even() -> None:
    """Ensures that only_evens returns only even numbers. Use Case."""
    evens: list[int] = [2, 3, 4, 6, 8, 9, 13]
    assert only_evens(evens) == [2, 4, 6, 8]


def test_only_evens_value() -> None:
    """Ensures function returns value. Edge Case."""
    evens: list[int] = [2]
    assert only_evens(evens) == [2]


def test_only_evens_odd_value() -> None:
    """Ensures that function returns nothing if only argument is odd. Use Case."""
    evens: list[int] = [3]
    assert only_evens(evens) == []


def test_sub_start_check() -> None:
    """Ensures that if start index is greater than list length, empty subset is returned. Use Case."""
    start: int = 3
    end: int = 1
    test_list: list[int] = [3, 5]
    assert sub(test_list, start, end) == []


def test_sub_end_check_zero() -> None:
    """Ensures that if end index is == 0, empty subset is returned. Use Case."""
    start: int = 1
    end: int = 0
    test_list: list[int] = [1, 2]
    assert sub(test_list, start, end) == []


def test_sub_end_check() -> None:
    """Ensures that if end index is < 0, empty subset returned. Use Case."""
    start: int = 1
    end: int = -1
    test_list: list[int] = [1, 2]
    assert sub(test_list, start, end) == []


def test_sub_empty_list() -> None:
    """Ensures empty list is returned if input list is empty. Use Case."""
    start: int = 1
    end: int = 2
    test_list: list[int] = []
    assert sub(test_list, start, end) == []


def test_sub_negative_start() -> None:
    """Ensures that if start index is negative, it is set to 0. Use Case."""
    start: int = -1
    end: int = 3
    test_list: list[int] = [1, 2, 3, 4]
    assert sub(test_list, start, end) == [1, 2, 3]


def test_sub_large_end() -> None:
    """Ensures that if end index is bigger than the list, it is set to length of list. Use Case."""
    start: int = 0
    end: int = 5
    test_list: list[int] = [1, 2, 3]
    assert sub(test_list, start, end) == [1, 2, 3]


def test_sub_work() -> None:
    """Ensures that a subset list is returned at appropriate indices. Use Case."""
    start: int = 1
    end: int = 4
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(test_list, start, end) == [2, 3, 4]


def test_sub_edge() -> None:
    """Ensures that if bounds are the length of the list, the same list is returned. Edge Case."""
    start: int = 0
    end: int = 5
    test_list: list[int] = [1, 2, 3, 4]
    assert sub(test_list, start, end) == [1, 2, 3, 4]

