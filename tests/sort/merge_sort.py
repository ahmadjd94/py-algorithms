from random import randint

from sorts import merge


def test_merge_sort():
    test_array = [randint(0, 10000) for i in range(1, 10**2)]
    result = merge(test_array)
    test_array.sort()
    assert test_array == result
