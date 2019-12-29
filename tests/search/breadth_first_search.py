from data_structures import Graph
from search.breadth_first_search import bfs


def test_bfs():
    a = Graph(["0", "1", "2", "3", "5", "6"], [
        ("0", "1"), ("1", "2"), ("1", "6"), ("2", "5"), ("2", "3")])

    assert bfs(a, "0", "7", set()) is False
    assert bfs(a, "0", "6", set()) is True
    assert bfs(a, "0", "3", set()) is True
    assert bfs(a, "0", "2", set()) is True
