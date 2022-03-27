"""Dictionary related utility functions."""

__author__ = "730397253"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a column-based table with only the requested number of rows."""
    if (rows >= len(table)):
        return table
    condensed: dict[str, list[str]] = {}
    for column in table:
        n_values: list[str] = []
        i: int = 0
        while (i < rows):
            n_values.append(table[column][i])
            i += 1
        condensed[column] = n_values
    return condensed


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a column-based table with only a specific subset of original columns."""
    subset: dict[str, list[str]] = {}
    i: int = 0
    while (i < len(names)):
        subset[names[i]] = table[names[i]]
        i += 1
    return subset


def concat(tab1: dict[str, list[str]], tab2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a column-based table with two tables merged (tab1 and tab2)."""
    merged: dict[str, list[str]] = {}
    for column in tab1:
        merged[column] = tab1[column]
    for column in tab2:
        if column in merged:
            merged[column] += tab2[column]
        else:
            merged[column] = tab2[column]
    return merged


def count(counting: list[str]) -> dict[str, int]:
    """Produces a dictionary that counts the number of times value repeats in list."""
    counted_val: dict[str, int] = {}
    i: int = 0
    while (i < len(counting)):
        if counting[i] in counted_val:
            counted_val[counting[i]] += 1
        else:
            counted_val[counting[i]] = 1
        i += 1
    return counted_val


def average(tab: dict[str, int]) -> float:
    """Returns a table of the averages of the input data set."""
    averages: float = 0.0
    total: float = 0
    divide_by: int = 0

    for key in tab:
        total += int(key) * tab[key]
        divide_by += tab[key] 
    averages = (total / divide_by)
    return averages