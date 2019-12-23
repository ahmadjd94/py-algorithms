import logging

from data_structures import Queue


def test_queue():
    f = Queue()
    logging.getLogger('logging').info('Testing Queue')
    test_array = [i for i in range(100)]

    for i in test_array:
        f.enqueue(i)

    result = []

    while not f.is_empty():
        result.append(f.deque())

    assert test_array == result
