from random import randint

from sorts import selection


def test_selection_sort():
    test_array = [randint(0, 10000) for i in range(0, 1000)]
    result = selection(test_array)
    test_array.sort()
    assert test_array == result
