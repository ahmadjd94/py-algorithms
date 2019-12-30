from math import floor


def binary_search(lst: list, target: int):
    l = len(lst)
    d = floor(l/2)

    if l == 1:
        return target == lst[0]
    elif l == 0:
        return False
    else:
        if target == lst[d]:
            return True
        elif target > lst[d]:
            return binary_search(lst[d:], target)
        elif target < lst[d]:
            return binary_search(lst[:d], target)

    return False
