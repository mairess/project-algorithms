from typing import Tuple


def quick_sort(string: list[str], start: int, end: int) -> None:
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)


def partition(entry: list[str], start: int, end: int):
    pivot = entry[end]
    delimiter = start - 1

    for index in range(start, end):
        if entry[index] <= pivot:
            delimiter = delimiter + 1
            entry[index], entry[delimiter] = entry[delimiter], entry[index]

    entry[delimiter + 1], entry[end] = entry[end], entry[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string: str, second_string: str) -> Tuple[str, str, bool]:
    if not first_string and not second_string:
        return ("", "", False)

    string_one = list(first_string.lower())
    string_two = list(second_string.lower())

    quick_sort(string_one, 0, len(string_one) - 1)
    quick_sort(string_two, 0, len(string_two) - 1)

    return (
        "".join(string_one),
        "".join(string_two),
        "".join(string_one) == "".join(string_two),
    )
