from data_structures import Stack


def test_stack():
    f = Stack()

    test_array = [i for i in range(100)]

    for i in test_array:
        f.push(i)

    result = []

    while not f.is_empty():
        result.append(f.pop())
    test_array.reverse()
    assert test_array == result
