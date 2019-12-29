from math import floor


def binary_search(lst: list, target: int):
    l = len(lst)
    d = floor(l/2)
    if l >= 1:
        if target > lst[d]:
            return binary_search(lst[d:], target)
        elif target < lst[d]:
            return binary_search(lst[:d], target)
        elif target == lst[d]:
            return True
    return False
