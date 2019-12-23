from data_structures import Stack
import logging


def test_stack():
    f = Stack()

    test_array = [i for i in range(100)]

    logging.getLogger('logging').info('Testing Stack')
    for i in test_array:
        f.push(i)

    result = []

    while not f.is_empty():
        result.append(f.pop())
    test_array.reverse()
    assert  test_array == result
