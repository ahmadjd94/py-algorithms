from copy import deepcopy
from random import randint

from sorts import insertion_sort


def test_insertion_sort():
    test_array = [randint(-10**7, 10000) for i in range(1, 10**2)]
    a = deepcopy(test_array)
    result = insertion_sort(test_array)
    a.sort()
    assert a == result
