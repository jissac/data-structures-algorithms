## BINARY SEARCH
## https://realpython.com/binary-search-python/
## time space complexity: https://iq.opengenus.org/time-complexity-of-binary-search/


from __future__ import annotations


def binary_search(items: [int], value: int) -> int | None:
    # find upper, middle, and lower boundaries
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if value == items[mid]:
            print(f"value: {value}, index: {mid}")
            return mid
        elif value > items[mid]:
            left = mid + 1
        elif value < items[mid]:
            right = mid - 1
    print("Value not in list of items")
    return None


def bs1(items: [int], value: int) -> int:
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == value:
            print(f"value found at index: {mid}")
            return mid
        elif items[mid] > value:
            right = mid - 1
        elif items[mid] < value:
            left = mid + 1
    print("Value not found in list")
    return -1


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    binary_search(input, 4)
    bs1(input, 4)
