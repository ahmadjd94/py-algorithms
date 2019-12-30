from search import binary_search


def test_binary_search():
    a = [i for i in range(2**10)]
    assert binary_search(a,5) is True
    assert binary_search(a,321) is True
    assert binary_search(a,-1) is False
    assert binary_search(a,0) is True
    assert binary_search(a,2**11) is False  #todo failing test case
