from random import randint

from sorts import bubble


def test_bubble_sort():
    test_array = [randint(-10**4, 10**3) for i in range(1, 10**2)]
    result = bubble(test_array)
    test_array.sort()
    assert test_array == result
