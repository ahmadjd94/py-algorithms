from copy import deepcopy
from random import randint

from sorts import quick_sort


def test_quick_sort():
    test_array = [randint(0, 1000000) for i in range(1, 10000)] # will crash on larger sizes
    test_array.sort()
    quick_sort(test_array, 0, len(test_array)-1)
    lst_copy = deepcopy(test_array)
    lst_copy.sort()
    assert test_array == lst_copy
