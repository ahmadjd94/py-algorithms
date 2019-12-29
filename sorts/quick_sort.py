from random import randrange


def partition(lst, low, high): # todo bug on large input sizes
    pivot = lst[high]
    i = low-1

    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[high] = lst[high], lst[i+1]

    return i+1


def rand_pivot(lst, low, high):
    p = randrange(low, high)
    lst[p], lst[low] = lst[low], lst[p]
    return partition(lst, low, high)


def quick_sort(lst, low, high):
    if low < high:
        ran = rand_pivot(lst, low, high)

        quick_sort(lst, low, ran-1)
        quick_sort(lst, ran+1, high)
