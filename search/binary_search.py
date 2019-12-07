from math import floor


def search(lst, target):
    l = len(lst)
    d = floor(l/2)
    if l >= 1:
        if target > lst[d]:
            return search(lst[d:], target)
        elif target < lst[d]:
            return search(lst[:d], target)
        elif target == lst[d]:
            return True
    return False
